Name:          libwebp6
Version:       0.5.2
Release:       1%{?dist}
URL:           http://webmproject.org/
Summary:       Library and tools for the WebP graphics format
# Additional IPR is licensed as well. See PATENTS file for details
License:       BSD
Source0:       http://downloads.webmproject.org/releases/webp/libwebp-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: freeglut-devel
BuildRequires: giflib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%autosetup -p1 -n libwebp-%{version}

%build
autoreconf -vif
%ifarch aarch64
export CFLAGS="%{optflags} -frename-registers"
%endif
# Neon disabled due to resulting CFLAGS conflict resulting in
# inlining failed in call to always_inline '[...]': target specific option mismatch
%configure \
  --disable-static \
  --disable-neon
%make_build

%install
mkdir -p %{buildroot}%{_libdir}
install -m 0755 -p src/.libs/libwebp.so.6* %{buildroot}%{_libdir}

%files -n %{name}
%license COPYING
%{_libdir}/libwebp.so.6*

%changelog
* Sat Jul 06 2024 Simone Caronni <negativo17@gmail.com> - 0.5.2-1
- First build.
