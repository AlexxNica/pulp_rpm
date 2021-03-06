Features
========

RPM Support includes a number of features that are not found in the generic
Pulp platform, the most important of which are described below.

Types
-----

Pulp RPM supports the following types:

* RPM
* DRPM
* SRPM
* Erratum
* Distribution
* Package Group
* Package Category

Errata
^^^^^^

.. push count? what is that?

`Red Hat <http://www.redhat.com>`_ provides security, bug fix, and enhancement
updates for supported Red Hat Enterprise products. These security updates are
provided through the Red Hat CDN, and are described by errata. Pulp supports
these errata types with a number of related features.

Errata are synchronized from upstream repositories. Errata can also be
:ref:`copied <copy-errata-recipe>` from one repository to another.
Administrators can also :ref:`upload <create-errata-recipe>` their own errata to
a repository. Please see the :doc:`recipes` documentation to learn how to
perform these operations.

Protected Repositories
----------------------

Red Hat protects its repositories with SSL-based
entitlement certificates. Pulp supports both ends of that operation:

Each Pulp repository can be configured with a client entitlement certificate and
key that it will use to retrieve packages from a remote repository. This is only
required when the remote repository is protected, such as when connecting to the
Red Hat CDN.

Pulp can be supplied a CA certificate that it will use to verify the authenticity
of client certificates when clients try to access Pulp-hosted repositories. This
is only required when you want to protect a Pulp-hosted repository. Repositories
can have these protection settings specified individually, or they can be set
globally for all RPM-related repositories.

For each Pulp-hosted repository that is protected, a consumer certificate can be
supplied that will be distributed to consumers when they bind. That certificate
will allow them to access the protected repository.

Package Signatures and GPG Key ID Filtering
-------------------------------------------

RPM repositories have limited support for acting on package GPG signatures,
including requiring packages to have GPG signatures, and whitelisting signing
key IDs to only sync packages with matching signing key IDs. The signing key
ID filtering feature uses the 8-character "short" key ID, which does not uniquely
identify a GPG signing key. This feature does not verify package signatures.

This signature filtering is granted within the current importer settings and current
import of the content, without taking into consideration content already present in
the repository.

These features cannot be enable with on_demand or background download policies, since
access to the package files is required to get the GPG signature information.
Only the immediate download policy is compatible with signature filtering.

Export
------

In addition to publishing repositories as normal yum repositories over HTTP or
HTTPS, it is also possible to export repositories to ISO images, which are published
over HTTP or HTTPS, or to a directory on the Pulp server. Large repositories may be
split into several ISOs.

Proxy Settings
--------------

When retrieving packages from a remote repository, Pulp can use a proxy and can
supply basic authentication credentials to that proxy.

Bandwidth Throttling
--------------------

When downloading packages from a remote source, Pulp can limit the speed at which
data is transferred. The number of downloader threads can also be specified.

