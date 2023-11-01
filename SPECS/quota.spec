# Use netlink to monitor quota usage and warn interactive users
%bcond_without quota_enables_netlink
# Enable getting quotas over remotely
%bcond_without quota_enables_rpc
# Allow setting quota remotely
%bcond_without quota_enables_rpcsetquota
# Disable TCP Wrappers guard in RPC quota daemon
%bcond_with quota_enables_tcpwrappers

Name:       quota
Epoch:      1
Version:    4.04
Release:    14%{?dist}
Summary:    System administration tools for monitoring users' disk usage
# quota_nld.c, quotaio_xfs.h:       GPLv2
# bylabel.c copied from util-linux: GPLv2+
# doc/quotas.ms, quotaops.c, quot.c, quotaon.c, edquota.c, quot.h, quota.c,
# quotaio_v1.c:                     BSD
# COPYING:                          GPLv2 text and license declaration
## Only in quota-rpc and quota-nls binary package
# svc_socket.c copied from glibc:   LGPLv2+
## Only in quota-nls binary package
# po/cs.po:                         GPLv2+
## Not involved in the binary package
# aclocal.m4:                       FSFULLR and (GPLv2+ with exception)
# ar-lib:                           GPLv2 with exception
# depcomp:                          GPLv2+ with exception
# config.guess:                     GPLv3+ with exception
# config.rpath:                     GPLv2+ with exception
# config.sub:                       GPLv3+ with exception
# configure:                        FSFUL
# install-sh:                       MIT
# m4/gettext.m4:                    GPL with exception
# m4/iconv.m4:                      GPL with exception
# m4/lib-ld.m4:                     GPL with exception
# m4/lib-link.m4:                   GPL with exception
# m4/lib-prefix.m4:                 GPL with exception
# m4/nls.m4:                        GPL with exception
# m4/po.m4:                         GPL with exception
# m4/progtest.m4:                   GPL with exception
# Makefile.in:                      FSFULLR
# missing:                          GPLv2+ with exception
# mkinstalldirs:                    Public Domain
License: BSD and GPLv2 and GPLv2+
URL: http://sourceforge.net/projects/linuxquota/
Source0: http://downloads.sourceforge.net/linuxquota/%{name}-%{version}.tar.gz
Source1: quota_nld.service
Source2: quota_nld.sysconfig
Source3: rpc-rquotad.service
Source4: rpc-rquotad.sysconfig
# Not accepted changes (378a64006bb1e818e84a1c77808563b802b028fa)
Patch0: quota-4.04-warnquota-configuration-tunes.patch
Patch1: quota-4.03-Validate-upper-bound-of-RPC-port.patch
# Install rquotad(3) only if RPC is enabled,
# <https://sourceforge.net/p/linuxquota/patches/45/>, in upstream after 4.04
Patch2: quota-4.04-Install-rquota-3-only-if-RPC-is-enabled.patch
# Pass TIRPC header files location to all RPC compilation units,
# <https://sourceforge.net/p/linuxquota/patches/46/>, in upstream after 4.04
Patch3: quota-4.04-Add-TIRPC_CFLAGS-globally-to-CFLAGS-for-RPC-support-.patch
# Do not iterate over negative UIDs in repquota,
# <https://sourceforge.net/p/linuxquota/patches/47/>, in upstream after 4.04
Patch4: quota-4.04-repquota-Fix-output-when-user-2-exists.patch
# Fix snprintf overflows in warnquota,
# <https://sourceforge.net/p/linuxquota/patches/48/>, in upstream after 4.04
Patch5: quota-4.04-warnquota-Check-snprintf-for-overflows.patch
# Fix user name search in utmp log,
# <https://sourceforge.net/p/linuxquota/patches/48/>, in upstream after 4.04
Patch6: quota-4.04-warnquota-Fix-comparing-user-name-to-non-null-termin.patch
# Avoid questions in quotacheck non-interactive mode, in upstream after 4.04
Patch7: quota-4.04-quotacheck-Avoid-question-in-non-interactive-mode.patch
# Report an error when quotacheck fails to cache quota files,
# in upstream after 4.04
Patch8: quota-4.04-quotacheck-Report-error-when-caching-of-quota-file-f.patch
# Report an error if quota file magic is invalid, in upstream after 4.04
Patch9: quota-4.04-quotacheck-Fail-check-if-quota-file-magic-is-invalid.patch
# Fix busy loop in rpc.rquotad, bug #1575956,
# <https://sourceforge.net/p/linuxquota/feature-requests/16/>
Patch10: quota-4.04-Listen-on-a-TCP-socket.patch
# Fix current block usage limit in RPC client, in upstream after 4.04,
# <https://sourceforge.net/p/linuxquota/bugs/127/>
Patch11: quota-4.04-rpc-Fix-wrong-limit-for-space-usage.patch
# Distinguish between none quota limits and no allocated resources in quota(1)
# tool output, proposed to upstream,
# <https://sourceforge.net/p/linuxquota/bugs/128/>
Patch12: quota-4.04-quota-1-Distinguish-between-none-quota-limits-and-no.patch
# Fix a descriptor leak, bug #1602674, proposed to upstream,
# <https://sourceforge.net/p/linuxquota/bugs/129/>
Patch13: quota-4.04-convertquota-Fix-a-file-descriptor-leak-in-convert_e.patch
# Fix a descriptor leak, bug #1602674, proposed to upstream,
# <https://sourceforge.net/p/linuxquota/bugs/129/>
Patch14: quota-4.04-quotackeck-Fix-a-directory-descriptor-leak-in-scan_d.patch
# Fix a descriptor leak, bug #1602674, proposed to upstream,
# <https://sourceforge.net/p/linuxquota/bugs/129/>
Patch15: quota-4.04-xqmstats-Fix-a-file-descriptor-leak-in-main.patch
# Pass quota type for Q_XFS_GETQSTAT, bug #1898549, in upstream after 4.05
Patch16: quota-4.05-quota-tools-pass-quota-type-to-QCMD-for-Q_XFS_GETQST.patch
# 1/2 Support setting individual grace times for XFS, bug #1898549,
# in upstream after 4.05
Patch17: quota-4.05-quota-tools-Set-FS_DQ_TIMER_MASK-for-individual-xfs-.patch
# 2/2 Support setting individual grace times for XFS, bug #1898549,
# in upstream after 4.05
Patch18: quota-4.05-Fix-limits-setting-on-XFS-filesystem.patch
# Add support for HPE XFS, bug #1945408, in upstream 4.05
Patch19: quota-4.04-Aadd-HPE-XFS-support.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  openldap-devel
%if %{with quota_enables_netlink}
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0) >= 3.1
BuildRequires:  pkgconfig(libnl-genl-3.0)
%endif
%if %{with quota_enables_rpc}
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  systemd
%if %{with quota_enables_tcpwrappers}
BuildRequires:  tcp_wrappers-devel
%endif
%endif
Requires:       quota-nls = %{epoch}:%{version}-%{release}
Conflicts:      kernel < 2.4

%description
The quota package contains system administration tools for monitoring
and limiting user and or group disk usage per file system.


%if %{with quota_enables_netlink}
%package nld
Summary:    quota_nld daemon
Requires:   quota-nls = %{epoch}:%{version}-%{release}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description nld
Daemon that listens on netlink socket and processes received quota warnings.
Note, that you have to enable the kernel support for sending quota messages
over netlink (in Filesystems->Quota menu). The daemon supports forwarding
warning messages to the system D-Bus (so that desktop manager can display
a dialog) and writing them to the terminal user has last accessed.
%endif


%if %{with quota_enables_rpc}
%package rpc
Summary:    RPC quota daemon
License:    BSD and LGPLv2+ and GPLv2 and GPLv2+
Requires:   quota-nls = %{epoch}:%{version}-%{release}
Requires:   rpcbind
%if %{with quota_enables_tcpwrappers}
Requires:   tcp_wrappers
%endif
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
Conflicts:  quota < 1:4.02-3

%description rpc
The RPC daemon allows to query and set disk quotas over network. If you run
the daemon on NFS server, you could use quota tools to manage the quotas from
NFS client.
%endif


%package warnquota
Summary:    Send e-mail to users over quota
Requires:   quota-nls = %{epoch}:%{version}-%{release}

%description warnquota
Utility that checks disk quota for each local file system and mails a warning
message to those users who have reached their soft limit.  It is typically run
via cron(8).


%package nls
Summary:    Gettext catalogs for disk quota tools
License:    BSD and LGPLv2+ and GPLv2 and GPLv2+
BuildArch:  noarch

%description nls
Disk quota tools messages translated into different natural languages.


%if %{with quota_enables_rpc}
%package devel
Summary:    Development files for quota RPC
License:    GPLv2
# libtirpc-devel for an included <rpc/rpc.h>
Requires:   libtirpc-devel
# Do not run-require main package, the header files define RPC API to be
# implemented by the developer, not an API for an existing quota library.

%description devel
This package contains development header files for implementing disk quotas
on remote machines.
%endif


%package doc
Summary:    Additional documentation for disk quotas
Requires:   quota =  %{epoch}:%{version}-%{release}
BuildArch:  noarch
AutoReq:    0

%description doc
This package contains additional documentation for disk quotas concept in
Linux/UNIX environment.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
# Regenerate build scripts
autoreconf -f -i

%build
%global _hardened_build 1
%configure \
    --enable-bsd-behaviour \
    --enable-ext2direct=yes \
    --enable-ldapmail=yes \
%if %{with quota_enables_tcpwrappers}
    --enable-libwrap=yes \
%else
    --disable-libwrap \
%endif
%if %{with quota_enables_netlink}
    --enable-netlink=yes \
%else
    --disable-netlink \
%endif
    --enable-nls \
    --disable-rpath \
%if %{with quota_enables_rpc}
    --enable-rpc=yes \
%else
    --disable-rpc \
%endif
%if %{with quota_enables_rpcsetquota}
    --enable-rpcsetquota=yes \
%else
    --disable-rpcsetquota \
%endif
    --disable-silent-rules \
    --disable-xfs-roothack
make


%install
make install DESTDIR=%{buildroot}
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with quota_enables_netlink}
install -p -m644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/quota_nld.service
install -p -m644 -D %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/quota_nld
%endif
%if %{with quota_enables_rpc}
install -p -m644 -D %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/rpc-rquotad.service
install -p -m644 -D %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rpc-rquotad
%endif

%find_lang %{name}


%check
make check


%if %{with quota_enables_netlink}
%post nld
%systemd_post quota_nld.service

%preun nld
%systemd_preun quota_nld.service

%postun nld
%systemd_postun_with_restart quota_nld.service
%endif


%if %{with quota_enables_rpc}
%post rpc
%systemd_post rpc-rquotad.service

%preun rpc
%systemd_preun rpc-rquotad.service

%postun rpc
%systemd_postun_with_restart rpc-rquotad.service
%endif


%files
%{_bindir}/*
%{_sbindir}/*
%exclude %{_sbindir}/quota_nld
%if %{with quota_enables_rpc}
%exclude %{_sbindir}/rpc.rquotad
%endif
%exclude %{_sbindir}/warnquota
%{_mandir}/man1/*
%{_mandir}/man8/*
%exclude %{_mandir}/man8/quota_nld.8*
%if %{with quota_enables_rpc}
%exclude %{_mandir}/man8/rpc.rquotad.8*
%endif
%exclude %{_mandir}/man8/warnquota.8*
%doc Changelog

%if %{with quota_enables_netlink}
%files nld
%config(noreplace) %{_sysconfdir}/sysconfig/quota_nld
%{_unitdir}/quota_nld.service
%{_sbindir}/quota_nld
%{_mandir}/man8/quota_nld.8*
%doc Changelog
%endif

%if %{with quota_enables_rpc}
%files rpc
%config(noreplace) %{_sysconfdir}/sysconfig/rpc-rquotad
%{_unitdir}/rpc-rquotad.service
%{_sbindir}/rpc.rquotad
%{_mandir}/man8/rpc.rquotad.8*
%doc Changelog
%endif

%files warnquota
%config(noreplace) %{_sysconfdir}/quotagrpadmins
%config(noreplace) %{_sysconfdir}/quotatab
%config(noreplace) %{_sysconfdir}/warnquota.conf
%{_sbindir}/warnquota
%{_mandir}/man5/*
%{_mandir}/man8/warnquota.8*
%doc Changelog README.ldap-support README.mailserver

%files nls -f %{name}.lang
# All the other packages require quota-nls, COPYING here is enough.
%license COPYING
%doc Changelog

%if %{with quota_enables_rpc}
%files devel
%license COPYING
%dir %{_includedir}/rpcsvc
%{_includedir}/rpcsvc/*
%{_mandir}/man3/*
%endif

%files doc
%doc doc/* ldap-scripts


%changelog
* Wed Apr 28 2021 Petr Pisar <ppisar@redhat.com> - 1:4.04-14
- Rebuild with binutils > 2.30-99 (bug #1954446)

* Tue Apr 06 2021 Petr Pisar <ppisar@redhat.com> - 1:4.04-13
- Add support for HPE XFS (bug #1945408)

* Wed Nov 18 2020 Petr Pisar <ppisar@redhat.com> - 1:4.04-12
- Support setting individual grace times for XFS (bug #1898549)

* Wed Sep 02 2020 Petr Pisar <ppisar@redhat.com> - 1:4.04-11
- Require libtirpc-devel by quota-devel because of rpc/rpc.h (bug #1868671)

* Thu Aug 23 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-10
- Fix file descriptor leaks in error code paths (bug #1602674)

* Tue Jul 24 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-9
- Distinguish between none quota limits and no allocated resources in quota(1)
  tool output

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-7
- Fix current block usage limit in RPC client

* Tue May 22 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-6
- Fix busy loop in rpc.rquotad (bug #1575956)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-4
- Avoid questions in quotacheck non-interactive mode
- Report an error when quotacheck fails to cache quota files
- Report an error if quota file magic is invalid

* Mon Feb 05 2018 Petr Pisar <ppisar@redhat.com> - 1:4.04-3
- rpcgen tool split from glibc-common package
- Pass TIRPC header files location to all RPC compilation units
- Do not iterate over negative UIDs in repquota
- Fix mistakes in warnquota reported by GCC 8

* Thu Nov 30 2017 Petr Pisar <ppisar@redhat.com> - 1:4.04-2
- Disable TCP wrappers (bug #1518778)

* Wed Sep 06 2017 Petr Pisar <ppisar@redhat.com> - 1:4.04-1
- 4.04 bump

* Mon Aug 28 2017 Petr Pisar <ppisar@redhat.com> - 1:4.03-12
- Fix memory leaks when running quotacheck on ext file systems (bug #1483543)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Petr Pisar <ppisar@redhat.com> - 1:4.03-9
- Fix disabling features at build time
- Fix a race between checking for and opening a directory to be scanned
- Fix an undefined behavior on parsing yes-no answer
- Check for setuid and setgid calls failure in edquota tool
- Check for failures when reading edquota input
- Check for failures when duplicating a file handle

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-7
- Fix checking a block read error (upstream bug #123)
- Use direct scanning also for ext4

* Fri Jun 10 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-6
- Correct repquota indentation for file systems with hiden quota files
- Remove unnecessary quota dependency from quota-devel package
- Break licenses down to each package

* Thu Mar 10 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-5
- Start rpc-rquotad.service when starting nfs-server.service

* Thu Mar 03 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-4
- Declare quota-rpc requires rpcbind because of the rpc.rquotad daemon

* Mon Feb 22 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-3
- Query kernel for next quota on XFS or file system with hidden quota files
  (bug #1306195)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Petr Pisar <ppisar@redhat.com> - 1:4.03-1
- 4.03 bump
- Work around Autoconf bug not to link ldap library to everything
  (bug #1296455)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 02 2015 Petr Pisar <ppisar@redhat.com> - 1:4.02-3
- Move rpc.rquotad daemon into quota-rpc sub-package

* Thu Apr 02 2015 Petr Pisar <ppisar@redhat.com> - 1:4.02-2
- Add rpc-rquotad.service file which was known as nfs-rquotad.service
  in nfs-utils (bug #1206260)

* Wed Nov 26 2014 Petr Pisar <ppisar@redhat.com> - 1:4.02-1
- 4.02 bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.01-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.01-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Petr Pisar <ppisar@redhat.com> - 1:4.01-12
- Prevent from grace period overflow in RPC transport (bug #1072769)

* Wed Oct 16 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-11
- Move /sbin/* files under /usr (bug #983179)
- Harden executables due to rpc.rquotad and quota_nld daemons (bug #983179)
- Document quotagrpadmins(5), quotatab(5), warnquota.conf(5), rcp.rquota(8)
  (bug #983179)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.01-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-9
- Close FILE handles on error too

* Wed Jun 12 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-8
- Allow to set limits using multiplicative units

* Mon May 27 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-7
- Add LGPLv2+ and GPLv2 to license declaration
- Correct changelog dates
- Package additional LDAP scripts as a documentation
- Package XFS-specific tools

* Mon May 20 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-6
- Remove code for migration from systemv-style init script
- Drop useless dependency on initscripts (bug #964440)

* Thu Mar 14 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-5
- Add quotasync(1) manual page
- Fix quota, repquota, and quotasync usage help

* Tue Feb 05 2013 Petr Pisar <ppisar@redhat.com> - 1:4.01-4
- Do not fiddle with quota files on XFS and GFS (bug #846296)
- Make sure option -d at quotacheck provides at least as much information as
  option -v (SF#3602777)

* Mon Dec 03 2012 Petr Pisar <ppisar@redhat.com> - 1:4.01-3
- Define charset in e-mails sent by warnquota (SF#3571589)

* Tue Sep 25 2012 Petr Pisar <ppisar@redhat.com> - 1:4.01-2
- Make group warning message more official

* Fri Sep 07 2012 Petr Pisar <ppisar@redhat.com> - 1:4.01-1
- 4.01 bump

* Wed Aug 22 2012 Petr Pisar <ppisar@redhat.com> - 1:4.00-6
- Modernize systemd scriptlets (bug #850288)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Petr Pisar <ppisar@redhat.com> - 1:4.00-4
- Fix editting more users with edquota
- Report all quotas on XFS (bug #837341)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep  1 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-2
- Remove unneeded cryptographic library build-time dependencies
- Fortify build-time configuration
- Migrate quota_nld service from sysvinit to systemd
- Document --print-below option in quota_nld service

* Tue Aug 23 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-1
- 4.00 bump
- Remove unneeded LDAP linking patch
- Prevent from stripping by configure option
- Remove unneeded sed scripts on sources
- Remove unneeded file removal

* Thu Aug 18 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.17.pre1
- Do not report missing utmp record to syslog (bug #731622)

* Fri Jul 15 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.16.pre1
- Report quotacheck failures by return code (bug #717982)
- Improve quotacheck error message (bug #717982)

* Thu May 12 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.15.pre1
- Make dirname static to work with nss_db (bug #703567)
- Clean spec file

* Mon Apr 11 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.14.pre1
- Initialize v2r1 ddquot padding in dump (bug #695409)
- Do not pass NULL to XGETQSTAT quotactl()

* Mon Mar 21 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.13.pre1
- Fix repquota to get latest quota info header (bug #689458)

* Fri Mar 11 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.12.pre1
- Fix ddquot buffer leak

* Thu Mar 10 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.11.pre1
- Disable grace period/times remote setting

* Mon Feb 28 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.10.pre1
- Do not use real domains in warnquota example

* Thu Feb 17 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.9.pre1
- Explain meaning of the second column in repquota output
- Make RPC handle properly host names with colons (i.e. IPv6 server host name)

* Wed Feb 09 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.8.pre1
- Initialize vfsold block and inode value boundries for new quota file
  (bug #668688)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.00-0.7.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.6.pre1
- Store quota_nld PID into PID file (bug #634137)
- Do not allow non-root to control quota_nld service (bug #634137)
- Add quotasync tool (bug #596794)
- Implement quotacheck for GFS2 (bug #596794)

* Wed Feb 02 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.5.pre1
- Correct manual pages

* Tue Jan 11 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.4.pre1
- Make RPC block factor dynamic (bug #667757)
- Check whether set limits fit into the range supported by quota format
  (bug #668688)
- Check set limits fit into the range supported by RPC transport (bug #668691)

* Mon Jan 10 2011 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.3.pre1
- Document --always-resolve option

* Tue Dec 14 2010 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.2.pre1
- Comment example quotatab to silent warnquota

* Tue Nov 16 2010 Petr Pisar <ppisar@redhat.com> - 1:4.00-0.1.pre1
- 4.00-pre1 bump
- Separate gettext catalogs becuase they are required by all binary sub-packages

* Mon Nov 15 2010 Petr Pisar <ppisar@redhat.com> - 1:3.17-18
- Break warnquota dependency on main package

* Mon Nov 15 2010 Petr Pisar <ppisar@redhat.com> - 1:3.17-17
- Convert Changelog to UTF-8

* Mon Nov 15 2010 Petr Pisar <ppisar@redhat.com> - 1:3.17-16
- Break dependecies on main package as there are none
- Add plain text documentation to each sub-package
- Package additional documentation into `doc' sub-package

* Thu Nov 11 2010 Petr Pisar <ppisar@redhat.com> - 1:3.17-15
- Add quota_nld daemon init script (bug #634169)
- Sub-package quota_nld files to weak dependecies
- Sub-package warnquota files to weak dependecies

* Wed Oct 06 2010 Petr Pisar <ppisar@redhat.com> - 1:3.17-14
- Remove quotactl(2) as it's part of `man-pages' package (bug #640590)

* Tue May 11 2010 Petr Pisar <ppisar@redhat.com> 1:3.17-13
- Add GFS2 support

* Mon May 10 2010 Petr Pisar <ppisar@redhat.com> 1:3.17-12
- Prevent corruptive read/write from/to NULL address in rpc.rquotad
  (Resolves #528581, example in #532342)
- Fix spelling in summary

* Fri Mar 12 2010 Daniel Novotny <dnovotny@redhat.com> 1:3.17-11
- the require from previous fix deleted altogether (it will
  be resolved automatically)

* Fri Mar 12 2010 Daniel Novotny <dnovotny@redhat.com> 1:3.17-10
- Requires: e2fsprogs changed to e2fsprogs-libs (#570005)

* Tue Feb 23 2010 Daniel Novotny <dnovotny@redhat.com> 1:3.17-9
- fix #565124 - FTBFS quota-3.17-8.fc13: ImplicitDSOLinking

* Tue Sep 29 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-8
- add buildrequires for quota_nld, enable-netlink to build
  quota_nld (#526047)

* Fri Sep 18 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-7
- Fix headers and structs in quotactl manpage(#524138)

* Fri Aug 28 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-6
- symlink manpage for rpc.rquotad

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 13 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-4
- clarify statements about LDAP in warnquota conf
  (related to #490106)
- fix parsing issue in warnquota.c(#490125)
- enable rpcsetquota by default(#159292, #469753)

* Fri Mar 13 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-3
- add missing buildrequires needed to compile with
  enable-ldapmail=try option with LDAP(#490106)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Ondrej Vasik <ovasik@redhat.com> 1:3.17-1
- new upstream release, remove already applied patches

* Mon Dec 08 2008 Ondrej Vasik <ovasik@redhat.com> 1:3.16-8
- fix documentation inconsistency (now rpc(3) instead of
  rpc(3N) in rquotad manpage) (#474836)

* Fri Nov 14 2008 Ondrej Vasik <ovasik@redhat.com> 1:3.16-7
- fix quotaoff --help output (was same as quotaon output)

* Thu Oct 30 2008 Ondrej Vasik <ovasik@redhat.com> 1:3.16-6
- fix implementation of ext4 support
  (by Mingming Cao, #469127)

* Wed Sep 10 2008 Ondrej Vasik <ovasik@redhat.com> 1:3.16-5
- fix rpmlint warnings - absolute symlink and not using epoch
  in version in changelog (#226353)
- rquota headers and manpage now in devel subpackage

* Wed Aug 27 2008 Ondrej Vasik <ovasik@redhat.com> 3.16-4
- fix bug in warnquota which could result in bogus hostname
  and domainname (upstream)
- remove IMMUTABLE flag from quota file in quotacheck(upstream)

* Tue Aug 05 2008 Ondrej Vasik <ovasik@redhat.com> 3.16-3
- Add support for -h option (do not show invalid option
  error) at edquota,setquota and quota (#457898)

* Fri Jun 20 2008 Ondrej Vasik <ovasik@redhat.com> 3.16-2
- upstream fix of some typos, string formats + 4TB+ fix
  for repquota
- some additional stripping removal
- change default mode of binaries from 555 to 755
  (strip error messages in build log)

* Wed Apr 23 2008 Ondrej Vasik <ovasik@redhat.com> 3.16-1
- own directory of rpcsvc headers(#442143)
- new upstream release

* Wed Mar 12 2008 Ondrej Vasik <ovasik@redhat.com> 3.15-6
- added enable-ldapmail=try option(wonder how #133207
  got closed by FC-4 without it or warnquota.conf change)
- dropped with-ext2direct=no option - this option is 
  invalid and original bug was fixed in 3.07

* Thu Mar  6 2008 Ondrej Vasik <ovasik@redhat.com> 3.15-5
- added symbolic link for quotaoff man page(#436110)
- don't ship xqmstats.8 man page as we don't ship those
  binaries(#436100)

* Thu Feb 21 2008 Ondrej Vasik <ovasik@redhat.com> 3.15-4
- added pointers to quota_nld and warnquota to some 
  manpages(upstream, #83975)

* Tue Feb 12 2008 Ondrej Vasik <ovasik@redhat.com> 3.15-3
- allow to build with rpcsetquota enabled(disabled by
  default, #159292)
- rebuild for gcc43

* Thu Jan 24 2008 Steve Dickson <SteveD@RedHat.com> 3.15-2
- More review comments:
    - BuiltPreReq to BuiltReq
    - Removed '.' From Summary
    - Added 'GPLv2+' to License Tag
    - Condensed the _sysconfdir entries in to one line

* Thu Jan 24 2008 Steve Dickson <SteveD@RedHat.com> 3.15-1
- Upgraded to version 3.15 
- Updated spec file per Merge Review (bz 226353)

* Thu Feb 15 2007  Steve Dickson <SteveD@RedHat.com> 3.14-1
- Upgraded to version 3.14 (bz# 213641)

* Mon Dec  4 2006 Thomas Woerner <twoerner@redhat.com> 1:3.13-1.3
- tcp_wrappers has a new devel and libs sub package, therefore changing build
  requirement for tcp_wrappers to tcp_wrappers-devel

* Wed Nov  1 2006 Steve Dickson <SteveD@RedHat.com> 1:3.13-1.2.3.2
- Added range checking on -p flag (bz 205145)
- Error message prints garbage characters (bz 201226)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:3.13-1.2.3.1
- rebuild

* Fri Jun 30 2006 Steve Dickson <steved@redhat.com> - 1:3.13-1.2.3
- fix 192826 - quota config files should not be overwritten

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:3.13-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:3.13-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 31 2005 Steve Dickson <steved@redhat.com> 3.13-1
- Upgraded to version 3.13 (bz# 171245)

* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- change the "Requires: kernel" into a "Conflicts:"

* Sun Sep 26 2004 Rik van Riel <riel@redhat.com> 3.12-5
- add URL (bz# 131862)

* Fri Sep 24 2004 Steve Dickson <SteveD@RedHat.com>
- Fixed typos in warnquota.conf patch 
  (bz# 82250 and bz# 83974)

* Mon Sep 13 2004 Steve Dickson <SteveD@RedHat.com>
- upgraded to 3.12

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- add -pie support
- update to 3.10

* Sat Aug 16 2003  Steve Dickson <SteveD@RedHat.com>
- upgraded to 3.0.9
- added quota-3.09-root_sbindir.patch

* Sun Aug 10 2003 Elliot Lee <sopwith@redhat.com> 3.06-11
- Rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 27 2003 Steve Dickson <SteveD@RedHat.com>
- rebuilt for 7.3 errata

* Tue Feb 25 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 23 2003 Tim Powers <timp@redhat.com>
- add buildprereq on tcp_wrappers

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches


* Fri Sep 6 2002 Philip Copeland <bryce@redhat.com> 3.06-5
- added --with-ext2direct=no to fix #73244
  without this users with UID's > 65535 will not
  be able to exist on a quota enabled FS

* Wed Aug 7 2002 Philip Copeland <bryce@redhat.com> 3.06-4
- Man page change. #60108

* Tue Aug 6 2002 Philip Copeland <bryce@redhat.com> 3.06-3
- Bah, I'd dropped epoch from the spec file but seems
  we need this if you want to upgrade as the epoch
  number has precedence over the version/release
  numbers.

* Wed Jul 17 2002 Philip Copeland <bryce@redhat.com> 3.06-2
- Lets stop the makefile from stripping the
  binaries as thats rpms job (apparently)

* Mon Jul 01 2002 Philip Copeland <bryce@redhat.com> 3.06-1
- Ditched the 3.01-pre9 src base for 3.06
  Rebuilt without any patchs

============================================================

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Elliot Lee <sopwith@redhat.com>
- IfArch the badkernelinclude patch for ppc-only.
- Update to 3.03

* Wed Dec 12 2001 Guy Streeter <streeter@redhat.com>
- Make #include of kernel header file work on non-x86

* Wed Sep  5 2001 Preston Brown <pbrown@redhat.com>
- require new initscripts

* Thu Aug 30 2001 Preston Brown <pbrown@redhat.com>
- fixed bug #52075 (problem with ext2 labels)
- backup data files off by default in quotacheck, optional backup flag added
- fix bug where giving a bad directory or device would cause 
  quotaon/quotacheck to simulate "-a" behaviour
- if a device name (i.e /dev/hda1) is passed, look up the corresponding mount
  point

* Wed Aug 29 2001 Preston Brown <pbrown@redhat.com>
- return an error code in more cases in convertquota

* Tue Aug 28 2001 Preston Brown <pbrown@redhat.com>
- 3.01pre9

* Fri Jul 20 2001 Preston Brown <pbrown@redhat.com>
- more cleanups on 3.01pre8

* Mon Jul  2 2001 Preston Brown <pbrown@redhat.com>
- 3.01 version, everything has changed again. :(

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Fri Mar 30 2001 Preston Brown <pbrown@redhat.com>
- use rpc.rquotad from here again (#33738)

* Thu Mar 15 2001 Preston Brown <pbrown@redhat.com>
- enable ALT_FORMAT for edquota

* Tue Mar 13 2001 Preston Brown <pbrown@redhat.com>
- I broke passing devices on the cmd line.  Fixed.

* Fri Mar 09 2001 Preston Brown <pbrown@redhat.com>
- quota 3.00 is required by recent kernel 2.4 changes
- no warnquota included this time, not yet ported
- quite a bit of work on quotacheck to make is backwards compatible
- we will likely go back to "quota 2.00" as these projects merge...

* Fri Feb 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- use "rm -f" instead of only "rm"

* Wed Feb  7 2001 Preston Brown <pbrown@redhat.com>
- fix quotacheck man page for -a option (#26380)

* Thu Feb  1 2001 Preston Brown <pbrown@redhat.com>
- 2.00 final, rolls in pretty much all our patches. :)
- fix reporting of in use dquot entries from quotastats
- change repquota man page to fix documentation of -v (#10330)
- include warnquota.conf

* Mon Nov 20 2000 Bill Nottingham <notting@redhat.com>
- fix ia64 build

* Mon Aug 21 2000 Jeff Johnson <jbj@redhat.com>
- add LABEL=foo support (#16390).

* Thu Jul 27 2000 Jeff Johnson <jbj@redhat.com>
- remote NFS quotas with different blocksize converted incorrectly (#11932).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 15 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Wed May 10 2000 Jeff Johnson <jbj@redhat.com>
- apply patch5 (H.J. Lu)

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Tue Jan 18 2000 Preston Brown <pbrown@redhat.com>
- quota 2.00 series
- removed unnecessary patches

* Thu Aug  5 1999 Jeff Johnson <jbj@redhat.com>
- fix man page FUD (#4369).

* Thu May 13 1999 Peter Hanecak <hanecak@megaloman.sk>
- changes to allow non-root users to build too (Makefile patch, %%attr)

* Tue Apr 13 1999 Jeff Johnson <jbj@redhat.com>
- fix for sparc64 quotas (#2147)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Mon Dec 28 1998 Cristian Gafton <gafton@redhat.com>
- don't install rpc.rquotad - we will use the one from the knfsd package
  instead

* Thu Dec 17 1998 Jeff Johnson <jbj@redhat.com>
- merge ultrapenguin 1.1.9 changes.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- removed patch for mntent

* Fri Mar 27 1998 Jakub Jelinek <jj@ultra.linux.cz>
- updated to quota 1.66

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- builds rquotad
- installs rpc.rquotad.8 symlink

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- removed /usr/include/rpcsvc/* from filelist
- uses a buildroot and %%attr

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Moved /usr/sbin/quota to /usr/bin/quota
