#!/bin/sh
# Make snapshot of webrtc
# Author: Elan Ruusamäe <glen@pld-linux.org>
set -e

# generate tarblla from svn
# try to be in sync with Chromium releases

package=webrtc
repo_url=http://$package.googlecode.com/svn/trunk
omahaproxy_url=http://omahaproxy.appspot.com
specfile=$package.spec

chrome_channel=${1:-stable}
chrome_version=$(curl -s "$omahaproxy_url/all?os=linux&channel=$chrome_channel" | awk -F, 'NR > 1{print $3}')
test -n "$chrome_version"
chrome_revision=$((echo 'data='; curl -s $omahaproxy_url/revision.json?version=$chrome_version; echo ',print(data.chromium_revision)') | js)
test -n "$chrome_revision"
chrome_branch=$(IFS=.; set -- $chrome_version; echo $3)
test -s DEPS.py || svn cat http://src.chromium.org/chrome/branches/$chrome_branch/src/DEPS@$chrome_revision > DEPS.py
webrtc_revision=$(awk -F'"' '/webrtc_revision.:/{print $4}' DEPS.py)
test -n "$webrtc_revision"

svn co $repo_url${webrtc_revision:+@$webrtc_revision} $package
svnrev=$(svnversion $package)
package_dir=$package-svn$svnrev
archive=$package_dir.tar.bz2

if [ -f $archive ]; then
	echo "Tarball $archive already exists"
	rm -f DEPS.py
	exit 0
fi

svn export $package $package_dir
tar -cjf $archive --exclude-vcs $package_dir
rm -rf $package_dir
../dropin $archive

rm -f DEPS.py
