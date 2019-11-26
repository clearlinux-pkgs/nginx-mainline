#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x520A9993A1C052F8 (mdounin@mdounin.ru)
#
Name     : nginx-mainline
Version  : 1.17.6
Release  : 99
URL      : https://nginx.org/download/nginx-1.17.6.tar.gz
Source0  : https://nginx.org/download/nginx-1.17.6.tar.gz
Source1  : nginx-mainline-setup.service
Source2  : nginx-mainline.service
Source3  : nginx-mainline.tmpfiles
Source4 : https://nginx.org/download/nginx-1.17.6.tar.gz.asc
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
Patch4: 0003-Add-nginx-module-build-install-script.patch

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


%package dev
Summary: dev components for the nginx-mainline package.
Group: Development
Requires: nginx-mainline-lib = %{version}-%{release}
Requires: nginx-mainline-bin = %{version}-%{release}
Requires: nginx-mainline-data = %{version}-%{release}
Provides: nginx-mainline-devel = %{version}-%{release}
Requires: nginx-mainline = %{version}-%{release}

%description dev
dev components for the nginx-mainline package.


%package extras-modulebuild
Summary: extras-modulebuild components for the nginx-mainline package.
Group: Default

%description extras-modulebuild
extras-modulebuild components for the nginx-mainline package.


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
%setup -q -n nginx-1.17.6
cd %{_builddir}/nginx-1.17.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574807544
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
--with-debug \
--error-log-path=stderr \
--with-file-aio \
--with-http_ssl_module \
--with-http_v2_module \
--with-poll_module \
--with-select_module \
--with-stream=dynamic \
--with-stream_ssl_module \
--with-http_realip_module \
--with-compat
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1574807544
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nginx-mainline
cp %{_builddir}/nginx-1.17.6/LICENSE %{buildroot}/usr/share/package-licenses/nginx-mainline/6e98d8b31beea6d51da2f8931062669945bd8aa4
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
mv %{buildroot}/var/www/html/* %{buildroot}/usr/share/nginx-mainline/html/ || :
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/nginx-mainline.service %{buildroot}/usr/share/clr-service-restart/nginx-mainline.service
install -m0755 nginx-module %{buildroot}/usr/bin
%{buildroot}/usr/bin/nginx-module asset-install %{buildroot}
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

%files dev
%defattr(-,root,root,-)
/usr/include/nginx-mainline/configure
/usr/include/nginx-mainline/core/nginx.h
/usr/include/nginx-mainline/core/ngx_array.h
/usr/include/nginx-mainline/core/ngx_buf.h
/usr/include/nginx-mainline/core/ngx_conf_file.h
/usr/include/nginx-mainline/core/ngx_config.h
/usr/include/nginx-mainline/core/ngx_connection.h
/usr/include/nginx-mainline/core/ngx_core.h
/usr/include/nginx-mainline/core/ngx_crc.h
/usr/include/nginx-mainline/core/ngx_crc32.h
/usr/include/nginx-mainline/core/ngx_crypt.h
/usr/include/nginx-mainline/core/ngx_cycle.h
/usr/include/nginx-mainline/core/ngx_file.h
/usr/include/nginx-mainline/core/ngx_hash.h
/usr/include/nginx-mainline/core/ngx_inet.h
/usr/include/nginx-mainline/core/ngx_list.h
/usr/include/nginx-mainline/core/ngx_log.h
/usr/include/nginx-mainline/core/ngx_md5.h
/usr/include/nginx-mainline/core/ngx_module.h
/usr/include/nginx-mainline/core/ngx_murmurhash.h
/usr/include/nginx-mainline/core/ngx_open_file_cache.h
/usr/include/nginx-mainline/core/ngx_palloc.h
/usr/include/nginx-mainline/core/ngx_parse.h
/usr/include/nginx-mainline/core/ngx_parse_time.h
/usr/include/nginx-mainline/core/ngx_proxy_protocol.h
/usr/include/nginx-mainline/core/ngx_queue.h
/usr/include/nginx-mainline/core/ngx_radix_tree.h
/usr/include/nginx-mainline/core/ngx_rbtree.h
/usr/include/nginx-mainline/core/ngx_regex.h
/usr/include/nginx-mainline/core/ngx_resolver.h
/usr/include/nginx-mainline/core/ngx_rwlock.h
/usr/include/nginx-mainline/core/ngx_sha1.h
/usr/include/nginx-mainline/core/ngx_shmtx.h
/usr/include/nginx-mainline/core/ngx_slab.h
/usr/include/nginx-mainline/core/ngx_string.h
/usr/include/nginx-mainline/core/ngx_syslog.h
/usr/include/nginx-mainline/core/ngx_thread_pool.h
/usr/include/nginx-mainline/core/ngx_times.h
/usr/include/nginx-mainline/event/ngx_event.h
/usr/include/nginx-mainline/event/ngx_event_connect.h
/usr/include/nginx-mainline/event/ngx_event_openssl.h
/usr/include/nginx-mainline/event/ngx_event_pipe.h
/usr/include/nginx-mainline/event/ngx_event_posted.h
/usr/include/nginx-mainline/event/ngx_event_timer.h
/usr/include/nginx-mainline/http/modules/ngx_http_ssi_filter_module.h
/usr/include/nginx-mainline/http/modules/ngx_http_ssl_module.h
/usr/include/nginx-mainline/http/modules/perl/ngx_http_perl_module.h
/usr/include/nginx-mainline/http/ngx_http.h
/usr/include/nginx-mainline/http/ngx_http_cache.h
/usr/include/nginx-mainline/http/ngx_http_config.h
/usr/include/nginx-mainline/http/ngx_http_core_module.h
/usr/include/nginx-mainline/http/ngx_http_request.h
/usr/include/nginx-mainline/http/ngx_http_script.h
/usr/include/nginx-mainline/http/ngx_http_upstream.h
/usr/include/nginx-mainline/http/ngx_http_upstream_round_robin.h
/usr/include/nginx-mainline/http/ngx_http_variables.h
/usr/include/nginx-mainline/http/v2/ngx_http_v2.h
/usr/include/nginx-mainline/http/v2/ngx_http_v2_module.h
/usr/include/nginx-mainline/mail/ngx_mail.h
/usr/include/nginx-mainline/mail/ngx_mail_imap_module.h
/usr/include/nginx-mainline/mail/ngx_mail_pop3_module.h
/usr/include/nginx-mainline/mail/ngx_mail_smtp_module.h
/usr/include/nginx-mainline/mail/ngx_mail_ssl_module.h
/usr/include/nginx-mainline/os/unix/ngx_alloc.h
/usr/include/nginx-mainline/os/unix/ngx_atomic.h
/usr/include/nginx-mainline/os/unix/ngx_channel.h
/usr/include/nginx-mainline/os/unix/ngx_darwin.h
/usr/include/nginx-mainline/os/unix/ngx_darwin_config.h
/usr/include/nginx-mainline/os/unix/ngx_dlopen.h
/usr/include/nginx-mainline/os/unix/ngx_errno.h
/usr/include/nginx-mainline/os/unix/ngx_files.h
/usr/include/nginx-mainline/os/unix/ngx_freebsd.h
/usr/include/nginx-mainline/os/unix/ngx_freebsd_config.h
/usr/include/nginx-mainline/os/unix/ngx_gcc_atomic_amd64.h
/usr/include/nginx-mainline/os/unix/ngx_gcc_atomic_ppc.h
/usr/include/nginx-mainline/os/unix/ngx_gcc_atomic_sparc64.h
/usr/include/nginx-mainline/os/unix/ngx_gcc_atomic_x86.h
/usr/include/nginx-mainline/os/unix/ngx_linux.h
/usr/include/nginx-mainline/os/unix/ngx_linux_config.h
/usr/include/nginx-mainline/os/unix/ngx_os.h
/usr/include/nginx-mainline/os/unix/ngx_posix_config.h
/usr/include/nginx-mainline/os/unix/ngx_process.h
/usr/include/nginx-mainline/os/unix/ngx_process_cycle.h
/usr/include/nginx-mainline/os/unix/ngx_setaffinity.h
/usr/include/nginx-mainline/os/unix/ngx_setproctitle.h
/usr/include/nginx-mainline/os/unix/ngx_shmem.h
/usr/include/nginx-mainline/os/unix/ngx_socket.h
/usr/include/nginx-mainline/os/unix/ngx_solaris.h
/usr/include/nginx-mainline/os/unix/ngx_solaris_config.h
/usr/include/nginx-mainline/os/unix/ngx_sunpro_atomic_sparc64.h
/usr/include/nginx-mainline/os/unix/ngx_thread.h
/usr/include/nginx-mainline/os/unix/ngx_time.h
/usr/include/nginx-mainline/os/unix/ngx_user.h
/usr/include/nginx-mainline/stream/ngx_stream.h
/usr/include/nginx-mainline/stream/ngx_stream_script.h
/usr/include/nginx-mainline/stream/ngx_stream_ssl_module.h
/usr/include/nginx-mainline/stream/ngx_stream_upstream.h
/usr/include/nginx-mainline/stream/ngx_stream_upstream_round_robin.h
/usr/include/nginx-mainline/stream/ngx_stream_variables.h

%files extras-modulebuild
%defattr(-,root,root,-)
/usr/bin/nginx-module
/usr/share/nginx-mainline/module-build/auto/cc/acc
/usr/share/nginx-mainline/module-build/auto/cc/bcc
/usr/share/nginx-mainline/module-build/auto/cc/ccc
/usr/share/nginx-mainline/module-build/auto/cc/clang
/usr/share/nginx-mainline/module-build/auto/cc/conf
/usr/share/nginx-mainline/module-build/auto/cc/gcc
/usr/share/nginx-mainline/module-build/auto/cc/icc
/usr/share/nginx-mainline/module-build/auto/cc/msvc
/usr/share/nginx-mainline/module-build/auto/cc/name
/usr/share/nginx-mainline/module-build/auto/cc/owc
/usr/share/nginx-mainline/module-build/auto/cc/sunc
/usr/share/nginx-mainline/module-build/auto/define
/usr/share/nginx-mainline/module-build/auto/endianness
/usr/share/nginx-mainline/module-build/auto/feature
/usr/share/nginx-mainline/module-build/auto/have
/usr/share/nginx-mainline/module-build/auto/have_headers
/usr/share/nginx-mainline/module-build/auto/headers
/usr/share/nginx-mainline/module-build/auto/include
/usr/share/nginx-mainline/module-build/auto/init
/usr/share/nginx-mainline/module-build/auto/install
/usr/share/nginx-mainline/module-build/auto/lib/conf
/usr/share/nginx-mainline/module-build/auto/lib/geoip/conf
/usr/share/nginx-mainline/module-build/auto/lib/google-perftools/conf
/usr/share/nginx-mainline/module-build/auto/lib/libatomic/conf
/usr/share/nginx-mainline/module-build/auto/lib/libatomic/make
/usr/share/nginx-mainline/module-build/auto/lib/libgd/conf
/usr/share/nginx-mainline/module-build/auto/lib/libxslt/conf
/usr/share/nginx-mainline/module-build/auto/lib/make
/usr/share/nginx-mainline/module-build/auto/lib/openssl/conf
/usr/share/nginx-mainline/module-build/auto/lib/openssl/make
/usr/share/nginx-mainline/module-build/auto/lib/openssl/makefile.bcc
/usr/share/nginx-mainline/module-build/auto/lib/openssl/makefile.msvc
/usr/share/nginx-mainline/module-build/auto/lib/pcre/conf
/usr/share/nginx-mainline/module-build/auto/lib/pcre/make
/usr/share/nginx-mainline/module-build/auto/lib/pcre/makefile.bcc
/usr/share/nginx-mainline/module-build/auto/lib/pcre/makefile.msvc
/usr/share/nginx-mainline/module-build/auto/lib/pcre/makefile.owc
/usr/share/nginx-mainline/module-build/auto/lib/perl/conf
/usr/share/nginx-mainline/module-build/auto/lib/perl/make
/usr/share/nginx-mainline/module-build/auto/lib/zlib/conf
/usr/share/nginx-mainline/module-build/auto/lib/zlib/make
/usr/share/nginx-mainline/module-build/auto/lib/zlib/makefile.bcc
/usr/share/nginx-mainline/module-build/auto/lib/zlib/makefile.msvc
/usr/share/nginx-mainline/module-build/auto/lib/zlib/makefile.owc
/usr/share/nginx-mainline/module-build/auto/make
/usr/share/nginx-mainline/module-build/auto/module
/usr/share/nginx-mainline/module-build/auto/modules
/usr/share/nginx-mainline/module-build/auto/nohave
/usr/share/nginx-mainline/module-build/auto/options
/usr/share/nginx-mainline/module-build/auto/os/conf
/usr/share/nginx-mainline/module-build/auto/os/darwin
/usr/share/nginx-mainline/module-build/auto/os/freebsd
/usr/share/nginx-mainline/module-build/auto/os/linux
/usr/share/nginx-mainline/module-build/auto/os/solaris
/usr/share/nginx-mainline/module-build/auto/os/win32
/usr/share/nginx-mainline/module-build/auto/sources
/usr/share/nginx-mainline/module-build/auto/stubs
/usr/share/nginx-mainline/module-build/auto/summary
/usr/share/nginx-mainline/module-build/auto/threads
/usr/share/nginx-mainline/module-build/auto/types/sizeof
/usr/share/nginx-mainline/module-build/auto/types/typedef
/usr/share/nginx-mainline/module-build/auto/types/uintptr_t
/usr/share/nginx-mainline/module-build/auto/types/value
/usr/share/nginx-mainline/module-build/auto/unix
/usr/share/nginx-mainline/module-build/configure

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_stream_module.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nginx-mainline/6e98d8b31beea6d51da2f8931062669945bd8aa4

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/nginx-mainline-setup.service
/usr/lib/systemd/system/nginx-mainline.service
