# pretix-custom-fonts

Custom fonts for internal poLANd.tf use on pretix. Initially we've been
modifying pretix-free-fonts package, but it's more suitable to have a separate
package in order to prevent handling merge conflicts from time to time in the
original package.
We use some proprietary fonts, therefore they are not available in the
repository itself and they are downloaded during a build process.

The package is heavily based on https://github.com/pretix/pretix-fontpack-free/