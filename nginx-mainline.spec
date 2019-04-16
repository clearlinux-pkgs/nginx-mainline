#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x520A9993A1C052F8 (mdounin@mdounin.ru)
#
Name     : nginx-mainline
Version  : 1.15.12
Release  : 76
URL      : https://nginx.org/download/nginx-1.15.12.tar.gz
Source0  : https://nginx.org/download/nginx-1.15.12.tar.gz
Source1  : nginx-mainline-setup.service
Source2  : nginx-mainline.service
Source3  : nginx-mainline.tmpfiles
Source99 : https://nginx.org/download/nginx-1.15.12.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: nginx-mainline-bin = %{version}-%{release}
Requires: nginx-mainline-config = %{version}-%{release}
Requires: nginx-mainline-data = %{version}-%{release}
Requires: nginx-mainline-lib = %{version}-%{release}
Requires: nginx-mainline-license = %{version}-%{release}
Requires: nginx-mainline-services = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : openssl-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
Patch1: build.patch
Patch2: 0001-Rework-nginx-configuration-directories.patch
Patch3: 0002-Enable-HTTP-2-by-default.patch

%description
Documentation is available at http://nginx.org

%package bin
Summary: bin components for the nginx-mainline package.
Group: Binaries
Requires: nginx-mainline-data = %{version}-%{release}
Requires: nginx-mainline-config = %{version}-%{release}
Requires: nginx-mainline-license = %{version}-%{release}
Requires: nginx-mainline-services = %{version}-%{release}

%description bin
bin components for the nginx-mainline package.


%package config
Summary: config components for the nginx-mainline package.
Group: Default

%description config
config components for the nginx-mainline package.


%package data
Summary: data components for the nginx-mainline package.
Group: Data

%description data
data components for the nginx-mainline package.


%package lib
Summary: lib components for the nginx-mainline package.
Group: Libraries
Requires: nginx-mainline-data = %{version}-%{release}
Requires: nginx-mainline-license = %{version}-%{release}

%description lib
lib components for the nginx-mainline package.


%package license
Summary: license components for the nginx-mainline package.
Group: Default

%description license
license components for the nginx-mainline package.


%package services
Summary: services components for the nginx-mainline package.
Group: Systemd services

%description services
services components for the nginx-mainline package.


%prep
%setup -q -n nginx-1.15.12
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555457535
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static --prefix=/var/www \
--conf-path=/usr/share/nginx-mainline/conf/nginx.conf \
--sbin-path=/usr/bin/nginx-mainline \
--pid-path=/run/nginx-mainline.pid \
--lock-path=/run/lock/nginx-mainline.lock \
--modules-path=/usr/lib64/nginx-mainline \
--http-log-path=syslog:server=unix:/dev/log \
--http-client-body-temp-path=/var/lib/nginx-mainline/client-body \
--http-fastcgi-temp-path=/var/lib/nginx-mainline/fastcgi \
--http-proxy-temp-path=/var/lib/nginx-mainline/proxy \
--http-scgi-temp-path=/var/lib/nginx-mainline/scgi \
--http-uwsgi-temp-path=/var/lib/nginx-mainline/uwsgi \
--user=httpd \
--group=httpd \
--with-threads \
--with-ipv6 \
--with-debug \
--error-log-path=stderr \
--with-file-aio \
--with-http_ssl_module \
--with-http_v2_module \
--with-poll_module \
--with-select_module \
--with-stream=dynamic \
--with-stream_ssl_module
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1555457535
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nginx-mainline
cp LICENSE %{buildroot}/usr/share/package-licenses/nginx-mainline/LICENSE
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/nginx-mainline-setup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/nginx-mainline.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/nginx-mainline.conf
## install_append content
rm -f %{buildroot}/usr/share/nginx-mainline/conf/*.default
install -m0644 conf/server.conf.example %{buildroot}/usr/share/nginx-mainline/conf/
install -m0644 conf/nginx.conf.example %{buildroot}/usr/share/nginx-mainline/conf/
mkdir -p %{buildroot}/usr/share/nginx-mainline/html
mv %{buildroot}/var/www/html/* %{buildroot}/usr/share/nginx-mainline/html/
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/nginx-mainline.service %{buildroot}/usr/share/clr-service-restart/nginx-mainline.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nginx-mainline

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/nginx-mainline.conf

%files data
%defattr(-,root,root,-)
/usr/share/clr-service-restart/nginx-mainline.service
/usr/share/nginx-mainline/conf/fastcgi.conf
/usr/share/nginx-mainline/conf/fastcgi_params
/usr/share/nginx-mainline/conf/koi-utf
/usr/share/nginx-mainline/conf/koi-win
/usr/share/nginx-mainline/conf/mime.types
/usr/share/nginx-mainline/conf/nginx.conf
/usr/share/nginx-mainline/conf/nginx.conf.example
/usr/share/nginx-mainline/conf/scgi_params
/usr/share/nginx-mainline/conf/server.conf.example
/usr/share/nginx-mainline/conf/uwsgi_params
/usr/share/nginx-mainline/conf/win-utf
/usr/share/nginx-mainline/html/50x.html
/usr/share/nginx-mainline/html/index.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_stream_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nginx-mainline/LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx-mainline-setup.service
/usr/lib/systemd/system/nginx-mainline.service
