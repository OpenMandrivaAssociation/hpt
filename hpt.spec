%global debug_package %{nil}
%define fver	1.4

%define pre	rc5
%define rel	1
%define release	0.%{pre}.%{rel}

Summary:	Highly Portable FTN Message Tosser
Name:           hpt
Version:        1.4.0
Release:        0.%{pre}.%{rel}
License:	GPLv2+
Group:		Networking/Other
Source0:		http://downloads.sourceforge.net/husky/%{name}-%{fver}-%{pre}.tar.gz
Patch0:		hpt-20021015-main.patch
Patch1:		hpt-20021015-doc.patch
patch2:		hpt-1.4-rc5.huskymak.patch
patch3:		hpt-1.4-rc5.printf.patch
Requires:	fidoconf
BuildRequires:	huskybse
BuildRequires:	smapi-devel
BuildRequires:	fidoconf-devel
BuildRequires:	texinfo
URL:		http://sourceforge.net/projects/husky/

%description
HPT is a Fidonet message tosser and packer with areafix.

Features of HPT:
 tossing packets of 2, 2.0 & 2+ types
 supporting of Msg, Squish and Jam message bases
 posting to net & echo areas
 areafix (on the fly, from command line, limit for areas...)
 autocreate on the fly
 forward requests
 pause and autopause for links
 linking of net & echo areas
 carbon copy
 groups & levels for personal and public access to echo areas
 powerful dupe checker
 link defaults

%prep
%setup -q -n %{name}
#% patch0 -p1
#% patch1 -p1
%patch2 -p1 -b .huskymak
%patch3 -p1 -b .printf

%build
%make OPTCFLAGS=" -c -fPIC %{optflags}"

%install
install -d %{buildroot}%{_bindir}
make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} install
make INFODIR=%{buildroot}%{_infodir} -C doc install
rm -rf %{buildroot}%{_infodir}/dir
install -d %{buildroot}%{_sysconfdir}/husky
install -m 644 config/{config,path,links,areas,packer} %{buildroot}%{_sysconfdir}/husky


%postun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc BUG-REPORTING BUGS COPYING CREDITS ChangeLog HISTORY INSTALL README TODO UPGRADE VERSION filter.pl config misc
%doc doc/{bugreport.rus,bugreport.txt,faqfmt.pl,hpt-FAQ.russian,perlwin32.rus,perlwin32.txt}
%attr(755,root,root) %{_bindir}/*
%{_infodir}/%{name}.info.*
%{_mandir}/*/*
%dir %{_sysconfdir}/husky
%config(noreplace) %{_sysconfdir}/husky/*



%changelog
* Sun Aug 24 2008 Adam Williamson <awilliamson@mandriva.com> 1.4.0-0.rc5.1mdv2009.0
+ Revision: 275520
- don't assume .bz2 extension for .info files
- new license policy
- replace $RPM_* with %%{*
- clean bracket use
- remove unncessary defines
- new prerelease 1.4.0-rc5

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import hpt

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Dec 07 2005 Lenny Cartier <lenny@mandriva.com> 1.4.0-0.rc2.3mdk
- rebuild

* Thu Jan  8 2004 Olivier Thauvin <nanardon@klama.mandrake.org> 1.4.0-0.rc2.2mdk
- Remove Requires: smapi 
- Fix perms

* Mon Dec 22 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.4.0-0.rc2.1mdk 
- cleanup
- From Iouri Goussev <elendal@polygonized.com>
  - First MDK version
  - original SPEC by Sergey Zhemchugov <Sergey_Zhemchugov@p8.f822.n463.z2.fidonet.org>
