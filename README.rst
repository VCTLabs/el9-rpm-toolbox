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

:daemonizer: https://sarnold.github.io/python-daemonizer/
:diskcache: http://www.grantjenks.com/docs/diskcache/
:honcho: https://honcho.readthedocs.io/
:picotui: https://sarnold.github.io/picotui/
:procman: https://sarnold.github.io/procman/
:py3tftp: https://github.com/sirMackk/py3tftp
:pygtail: https://github.com/VCTLabs/pygtail
:pyprctrl: https://pyprctl.readthedocs.io/en/latest
:stoppy: https://github.com/morefigs/stoppy
:timed-count: https://github.com/morefigs/timed-count
:tftpy: https://msoulier.github.io/tftpy/pages/html/
