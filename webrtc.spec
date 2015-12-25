%define		svndate	20121218
# Chromium 23 needs this revision.
%define		svnrev	2718
Summary:	Libraries to provide Real Time Communications via the web
Name:		webrtc
Version:	0.1
Release:	0.13.%{svndate}svn%{svnrev}
License:	BSD
Group:		Libraries
URL:		http://www.webrtc.org/
# No source tarballs. This is a google failure^Wproject.
# svn export http://webrtc.googlecode.com/svn/trunk/ webrtc
# mv webrtc/ webrtc-20120613svn2401
# tar cfj webrtc-20120613svn2401.tar.bz2 webrtc-20120613svn2401
Source0:	%{name}-%{svndate}svn%{svnrev}.tar.bz2
# Source0-md5:	68977feca42feea6f358aeaf4c463880
# Google provides no real way to build this code, except as part of Chromium
# That's just stupid.
Patch0:		build-sanity.patch
Patch1:		libvpx2.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvpx-devel
BuildRequires:	libyuv-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# various missing libs: -lpthread, -lm, -lX11 ...
%define		skip_post_check_so	libsystem_wrappers.so.*.*.* libiSAC.so.*.*.* libwebrtc_utility.so.*.*.* libapm_util.so.*.*.* libaec.so.*.*.* libns.so.*.*.* libbitrate_controller.so.*.*.* libvideo_render_module.so.*.*.* libwebrtc_jpeg.so.*.*.* libwebrtc_i420.so.*.*.*

%description
WebRTC is a free, open project that enables web browsers with
Real-Time Communications (RTC) capabilities via simple Javascript
APIs. The WebRTC components have been optimized to best serve this
purpose.

%package devel
Summary:	Development files for WebRTC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-turbo-devel
Requires:	libvpx-devel
Requires:	libyuv-devel

%description devel
Development files for WebRTC.

%prep
%setup -q -n %{name}-%{svndate}svn%{svnrev}
touch NEWS README ChangeLog
ln -s LICENSE COPYING
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	%{nil}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE PATENTS AUTHORS
%attr(755,root,root) %{_bindir}/frame_analyzer
%attr(755,root,root) %{_bindir}/psnr_ssim_analyzer
%attr(755,root,root) %{_bindir}/rgba_to_i420_converter

%attr(755,root,root) %{_libdir}/libCNG.so.*.*.*
%ghost %{_libdir}/libCNG.so.0
%attr(755,root,root) %{_libdir}/libG711.so.*.*.*
%ghost %{_libdir}/libG711.so.0
%attr(755,root,root) %{_libdir}/libG722.so.*.*.*
%ghost %{_libdir}/libG722.so.0
%attr(755,root,root) %{_libdir}/libNetEq.so.*.*.*
%ghost %{_libdir}/libNetEq.so.0
%attr(755,root,root) %{_libdir}/libPCM16B.so.*.*.*
%ghost %{_libdir}/libPCM16B.so.0
%attr(755,root,root) %{_libdir}/libaec.so.*.*.*
%ghost %{_libdir}/libaec.so.0
%attr(755,root,root) %{_libdir}/libaecm.so.*.*.*
%ghost %{_libdir}/libaecm.so.0
%attr(755,root,root) %{_libdir}/libagc.so.*.*.*
%ghost %{_libdir}/libagc.so.0
%attr(755,root,root) %{_libdir}/libapm_util.so.*.*.*
%ghost %{_libdir}/libapm_util.so.0
%attr(755,root,root) %{_libdir}/libaudio_coding_module.so.*.*.*
%ghost %{_libdir}/libaudio_coding_module.so.0
%attr(755,root,root) %{_libdir}/libaudio_conference_mixer.so.*.*.*
%ghost %{_libdir}/libaudio_conference_mixer.so.0
%attr(755,root,root) %{_libdir}/libaudio_device.so.*.*.*
%ghost %{_libdir}/libaudio_device.so.0
%attr(755,root,root) %{_libdir}/libaudio_processing.so.*.*.*
%ghost %{_libdir}/libaudio_processing.so.0
%attr(755,root,root) %{_libdir}/libbitrate_controller.so.*.*.*
%ghost %{_libdir}/libbitrate_controller.so.0
%attr(755,root,root) %{_libdir}/libiLBC.so.*.*.*
%ghost %{_libdir}/libiLBC.so.0
%attr(755,root,root) %{_libdir}/libiSAC.so.*.*.*
%ghost %{_libdir}/libiSAC.so.0
%attr(755,root,root) %{_libdir}/libiSACFix.so.*.*.*
%ghost %{_libdir}/libiSACFix.so.0
%attr(755,root,root) %{_libdir}/libmedia_file.so.*.*.*
%ghost %{_libdir}/libmedia_file.so.0
%attr(755,root,root) %{_libdir}/libns.so.*.*.*
%ghost %{_libdir}/libns.so.0
%attr(755,root,root) %{_libdir}/libremote_bitrate_estimator.so.*.*.*
%ghost %{_libdir}/libremote_bitrate_estimator.so.0
%attr(755,root,root) %{_libdir}/libresampler.so.*.*.*
%ghost %{_libdir}/libresampler.so.0
%attr(755,root,root) %{_libdir}/librtp_rtcp.so.*.*.*
%ghost %{_libdir}/librtp_rtcp.so.0
%attr(755,root,root) %{_libdir}/libsignal_processing.so.*.*.*
%ghost %{_libdir}/libsignal_processing.so.0
%attr(755,root,root) %{_libdir}/libsimple_command_line_parser.so.*.*.*
%ghost %{_libdir}/libsimple_command_line_parser.so.0
%attr(755,root,root) %{_libdir}/libsystem_wrappers.so.*.*.*
%ghost %{_libdir}/libsystem_wrappers.so.0
%attr(755,root,root) %{_libdir}/libudp_transport.so.*.*.*
%ghost %{_libdir}/libudp_transport.so.0
%attr(755,root,root) %{_libdir}/libvad.so.*.*.*
%ghost %{_libdir}/libvad.so.0
%attr(755,root,root) %{_libdir}/libvideo_capture_module.so.*.*.*
%ghost %{_libdir}/libvideo_capture_module.so.0
%attr(755,root,root) %{_libdir}/libvideo_engine_core.so.*.*.*
%ghost %{_libdir}/libvideo_engine_core.so.0
%attr(755,root,root) %{_libdir}/libvideo_processing.so.*.*.*
%ghost %{_libdir}/libvideo_processing.so.0
%attr(755,root,root) %{_libdir}/libvideo_quality_analysis.so.*.*.*
%ghost %{_libdir}/libvideo_quality_analysis.so.0
%attr(755,root,root) %{_libdir}/libvideo_render_module.so.*.*.*
%ghost %{_libdir}/libvideo_render_module.so.0
%attr(755,root,root) %{_libdir}/libvoice_engine_core.so.*.*.*
%ghost %{_libdir}/libvoice_engine_core.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_i420.so.*.*.*
%ghost %{_libdir}/libwebrtc_i420.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_jpeg.so.*.*.*
%ghost %{_libdir}/libwebrtc_jpeg.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_libyuv.so.*.*.*
%ghost %{_libdir}/libwebrtc_libyuv.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_utility.so.*.*.*
%ghost %{_libdir}/libwebrtc_utility.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_video_coding.so.*.*.*
%ghost %{_libdir}/libwebrtc_video_coding.so.0
%attr(755,root,root) %{_libdir}/libwebrtc_vp8.so.*.*.*
%ghost %{_libdir}/libwebrtc_vp8.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/webrtc
%{_libdir}/libCNG.so
%{_libdir}/libG711.so
%{_libdir}/libG722.so
%{_libdir}/libNetEq.so
%{_libdir}/libPCM16B.so
%{_libdir}/libaec.so
%{_libdir}/libaecm.so
%{_libdir}/libagc.so
%{_libdir}/libapm_util.so
%{_libdir}/libaudio_coding_module.so
%{_libdir}/libaudio_conference_mixer.so
%{_libdir}/libaudio_device.so
%{_libdir}/libaudio_processing.so
%{_libdir}/libbitrate_controller.so
%{_libdir}/libiLBC.so
%{_libdir}/libiSAC.so
%{_libdir}/libiSACFix.so
%{_libdir}/libmedia_file.so
%{_libdir}/libns.so
%{_libdir}/libremote_bitrate_estimator.so
%{_libdir}/libresampler.so
%{_libdir}/librtp_rtcp.so
%{_libdir}/libsignal_processing.so
%{_libdir}/libsimple_command_line_parser.so
%{_libdir}/libsystem_wrappers.so
%{_libdir}/libudp_transport.so
%{_libdir}/libvad.so
%{_libdir}/libvideo_capture_module.so
%{_libdir}/libvideo_engine_core.so
%{_libdir}/libvideo_processing.so
%{_libdir}/libvideo_quality_analysis.so
%{_libdir}/libvideo_render_module.so
%{_libdir}/libvoice_engine_core.so
%{_libdir}/libwebrtc_i420.so
%{_libdir}/libwebrtc_jpeg.so
%{_libdir}/libwebrtc_libyuv.so
%{_libdir}/libwebrtc_utility.so
%{_libdir}/libwebrtc_video_coding.so
%{_libdir}/libwebrtc_vp8.so
