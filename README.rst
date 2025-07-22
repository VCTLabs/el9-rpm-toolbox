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


.. table:: RPM build status
   :widths: auto

   =============  ===============
    Package        Status
   =============  ===============
    daemonizer     |daemonizer|
    diskcache      |diskcache|
    honcho         |honcho|
    picotui        |picotui|
    procman        |procman|
    py3tftp        |py3tftp|
    pygtail        |pygtail|
    pyprctrl       |pyprctrl|
    pyserv         |pyserv|
    stoppy         |stoppy|
    timed-count    |timed-count|
    tftpy          |tftpy|
   =============  ===============


.. |daemonizer| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/daemonizer.yml/badge.svg
    :target: https://sarnold.github.io/python-daemonizer/
    :alt: daemonizer RPM status

.. |diskcache| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/diskcache.yml/badge.svg
    :target: http://www.grantjenks.com/docs/diskcache/
    :alt: diskcache RPM status

.. |honcho| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/honcho.yml/badge.svg
    :target: https://honcho.readthedocs.io/
    :alt: honcho RPM status

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

.. |pyprctrl| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/pyprctrl.yml/badge.svg
    :target: https://pyprctl.readthedocs.io/en/latest
    :alt: pyprctrl RPM status

.. |pyserv| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/pyserv.yml/badge.svg
    :target: https://sarnold.github.io/pyserv/
    :alt: pyserv RPM status

.. |stoppy| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/stoppy.yml/badge.svg
    :target: https://github.com/morefigs/stoppy
    :alt: stoppy RPM status

.. |timed-count| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/timed-count.yml/badge.svg
    :target: https://github.com/morefigs/timed-count
    :alt: timed-count RPM status

.. |tftpy| image:: https://github.com/VCTLabs/el9-rpm-toolbox/actions/workflows/tftpy.yml/badge.svg
    :target: https://msoulier.github.io/tftpy/pages/html/
    :alt: tftpy RPM status
