""" Code to generate doc/topics.rst during 'sphinx-build'.

This code:

- Uses :mod:`nose` to find all the fedmsg.meta unittests.
- Extracts all the metadata and docstrings from those tests.
- Uses all that to generate a giant .rst document of all the fedmsg
  topics and what they are about with example messages.

"""

import os
import nose
import pprint
import textwrap

header = """
List of Message Topics
======================

.. DO NOT EDIT THIS DOCUMENT.

.. It is autogenerated from fedmsg_meta_fedora_infrastructure/doc_utilities.py

This document lists all the topics coming out the Fedora
Infrastructure fedmsg bus.  Example messages are included
as well as descriptions and sample output from ``fedmsg.meta``.

.. note:: All topics from Fedora Infrastructure are prefixed with
   ``org.fedoraproject.prod.``, but the :term:`topic_prefix` is omitted here
   for brevity.  For instance, the item listed as ``git.branch`` will
   actually be broadcast as ``org.fedoraproject.prod.git.branch``.

.. note:: Message bodies can contain some useful information, but be wary.
   We have done as good a job as we can *securing* fedmsg, but it is still
   a new system.  If you receive a message from pkgdb claiming that "ralph"
   is the new owner of the kernel, you should still *check* with the *actual*
   pkgdb service that this is the case.  Write code against fedmsg messages
   as a tip, but always check the authoritative source before taking any
   programmatic action.

"""

metadata_template = """
The example message above, when passed to various routines in the
:mod:`fedmsg.meta` module, will produce the following outputs:

- :func:`fedmsg.meta.msg2title`

  - {title}

- :func:`fedmsg.meta.msg2subtitle`

  - {subtitle}

- :func:`fedmsg.meta.msg2link`

  - {link}

- :func:`fedmsg.meta.msg2icon`

  - {icon}

- :func:`fedmsg.meta.msg2secondary_icon`

  - {secondary_icon}

- :func:`fedmsg.meta.msg2usernames`

 - ``{usernames}``

- :func:`fedmsg.meta.msg2packages`

 - ``{packages}``

- :func:`fedmsg.meta.msg2objects`

 - ``{objects}``

"""

outfile = None


def write(fname, s=''):
    global outfile
    if not outfile:
        outfile = open(fname, 'w')

    outfile.write(s + '\n')


def load_classes(folder):
    return list(list(
        nose.loader.defaultTestLoader().loadTestsFromDir(folder)
    )[0])


def make_topics_doc(output_dir):

    fname = output_dir + "/topics.rst"

    global outfile
    import fedmsg_meta_fedora_infrastructure
    filename = fedmsg_meta_fedora_infrastructure.__file__
    folder = os.path.sep + os.path.join(*filename.split('/')[:-1])
    test_classes = load_classes(folder)

    # TODO -- get the logger and announce messages
    #import fedmsg
    #filename = fedmsg.__file__
    #folder = os.path.sep + os.path.join(*filename.split('/')[:-1])
    #test_classes = load_classes(folder)

    write(fname, header)

    for cls in test_classes:
        if cls.context.msg:

            # Adjust {stg,dev} to prod.
            cls.context.msg['topic'] = cls.context.msg['topic']\
                .replace('.stg.', '.prod.')\
                .replace('.dev.', '.prod.')
            cls.context.expected_title = cls.context.expected_title\
                .replace('.stg.', '.prod.')\
                .replace('.dev.', '.prod.')

            topic = '.'.join(cls.context.msg['topic'].split('.')[3:])
            cls.__topic = topic
        else:
            cls.__topic = None

    comparator = lambda a, b: cmp(a.__topic, b.__topic)
    test_classes = sorted(test_classes, comparator)

    seen = []
    for cls in test_classes:
        if cls.context.msg:
            topic = cls.__topic

            # Ignore tests that check old messages.
            if 'Legacy' in cls.context.__name__:
                continue

            modname = topic.split('.')[0]
            if not modname in seen:
                seen.append(modname)
                write(fname, modname)
                write(fname, "-" * len(modname))
                write(fname)

            write(fname, topic)
            write(fname, "~" * len(topic))
            write(fname)

            # I would use __doc__ here, but something that nose is doing is
            # stripping the __doc__ from my original unit tests.  Instead,
            # we'll use our own 'doc' attribute which is a little clumsy.
            if getattr(cls.context, 'doc', None):
                write(fname, textwrap.dedent("    " + cls.context.doc.strip()))
                write(fname)

            write(fname, ".. code-block:: python")
            write(fname, '\n    ' + pprint.pformat(cls.context.msg, indent=2)
                  .replace('\n', '\n    '))
            write(fname)
            write(fname, metadata_template.format(
                link=cls.context.expected_link,
                title=cls.context.expected_title,
                subtitle=cls.context.expected_subti,
                usernames=cls.context.expected_usernames,
                packages=cls.context.expected_packages,
                objects=cls.context.expected_objects,
                icon=cls.context.expected_icon,
                secondary_icon=cls.context.expected_secondary_icon,
            ))
            write(fname)

    outfile.close()

if __name__ == '__main__':
    make_topics_doc()
