el9 RPM toolbox
===============

This repository includes "extra" prebuilt RPM packages and spec files for
various tools like diskcache and pygtail.

RPM builds are done automatically with GitHub Actions. The packages are
uploaded to the `release section`_ each time there is a new version (tag).
The artifacts are also available in the artifacts of each GitHub Action.

.. _release section: https://github.com/VCTLabs/el9-rpm-toolbox/releases

However, there are some limitations to using the artifacts directly:

* Downloading of build artifacts in GitHub Ations currently requires a
  GitHub account
* Blobs in build artifacts are zipped by the GitHub frontend by default,
  even zip files themselves! Build artifact zips may contain other zip
  files
* Build artifacts will expire after some time

Therefore, it is recommended to download the binaries from the release
section. This repo is intended primarily for Python project dependencies;
issues requesting new packages will be considered based on time available,
however, Pull Requests are the preferred mechanism for contributions.

Look in the releases for the latest versioned RPMs for each spec in the
following table.

Note the example configuration for RPMGet_ contains the URLs for all
toolbox rpms (which you can use to download them to an install target
or RPM repo host).

.. _RPMGet: https://github.com/sarnold/rpmget

.. table:: RPM build status
   :widths: auto

   ==============  ==================
    Package         Status
   ==============  ==================
    atomics         |atomics|
    daemonizer      |daemonizer|
    diskcache       |diskcache|
    hexdump         |hexdump|
    honcho          |honcho|
    line_profiler   |line_profiler|
    logwatcher      |logwatcher|
    picotui         |picotui|
    procman         |procman|
    py3tftp         |py3tftp|
    pyeztrace       |pyeztrace|
    pygtail         |pygtail|
    pyprctl         |pyprctl|
    pyserv          |pyserv|
    rpmget          |rpmget|
    stoppy          |stoppy|
    timed-count     |timed-count|
    tftpy           |tftpy|
   ==============  ==================


.. |atomics| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/atomics.yml/badge.svg
    :target: https://github.com/doodspav/atomics
    :alt: atomics RPM status

.. |daemonizer| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/daemonizer.yml/badge.svg
    :target: https://sarnold.github.io/python-daemonizer/
    :alt: daemonizer RPM status

.. |diskcache| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/diskcache.yml/badge.svg
    :target: http://www.grantjenks.com/docs/diskcache/
    :alt: diskcache RPM status

.. |pyeztrace| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/eztrace.yml/badge.svg
    :target: https://github.com/jeffersonaaron25/PyEzTrace
    :alt: pyeztrace RPM status

.. |hexdump| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/hexdump.yml/badge.svg
    :target: https://sarnold.github.io/hexdump/
    :alt: hexdump RPM status

.. |honcho| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/honcho.yml/badge.svg
    :target: https://honcho.readthedocs.io/
    :alt: honcho RPM status

.. |line_profiler| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/line_profiler.yml/badge.svg
    :target: https://github.com/pyutils/line_profiler
    :alt: line_profiler RPM status

.. |logwatcher| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/logwatcher.yml/badge.svg
    :target: https://github.com/sarnold/pylogtailer
    :alt: logwatcher RPM status

.. |picotui| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/picotui.yml/badge.svg
    :target: https://sarnold.github.io/picotui/
    :alt: picotui RPM status

.. |procman| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/procman.yml/badge.svg
    :target: https://sarnold.github.io/procman/
    :alt: procman RPM status

.. |py3tftp| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/py3tftp.yml/badge.svg
    :target: https://github.com/sirMackk/py3tftp
    :alt: py3tftp RPM status

.. |pygtail| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/pygtail.yml/badge.svg
    :target: https://github.com/VCTLabs/pygtail
    :alt: pygtail RPM status

.. |pyprctl| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/pyprctl.yml/badge.svg
    :target: https://pyprctl.readthedocs.io/en/latest
    :alt: pyprctl RPM status

.. |pyserv| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/pyserv.yml/badge.svg
    :target: https://sarnold.github.io/pyserv/
    :alt: pyserv RPM status

.. |rpmget| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/rpmget.yml/badge.svg
    :target: https://sarnold.github.io/rpmget/
    :alt: rpmget RPM status

.. |stoppy| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/stoppy.yml/badge.svg
    :target: https://github.com/morefigs/stoppy
    :alt: stoppy RPM status

.. |timed-count| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/timed-count.yml/badge.svg
    :target: https://github.com/morefigs/timed-count
    :alt: timed-count RPM status

.. |tftpy| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/tftpy.yml/badge.svg
    :target: https://msoulier.github.io/tftpy/pages/html/
    :alt: tftpy RPM status
