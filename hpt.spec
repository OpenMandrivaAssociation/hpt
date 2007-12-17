%define name    hpt
%define version 1.4.0
%define preversion rc2

%define rel  %mkrel 
%define release 0.%{preversion}.%rel

Summary:	Highly Portable FTN Message Tosser
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Group:		Networking/Other
Source:		%{name}-%{version}%{preversion}.tar.bz2
Patch0:		hpt-20021015-main.patch.bz2
Patch1:		hpt-20021015-doc.patch.bz2
Requires:	fidoconf
BuildRequires:	huskybse, smapi-devel, fidoconf-devel, texinfo
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
%setup -q -n %name
%patch0 -p1
%patch1 -p1

%build
%make OPTCFLAGS=" -s -c -fPIC $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
make BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir} install
make INFODIR=$RPM_BUILD_ROOT%{_infodir} -C doc install
rm -rf $RPM_BUILD_ROOT%{_infodir}/dir
install -d $RPM_BUILD_ROOT%{_sysconfdir}/husky
install -m 644 config/{config,path,links,areas,packer} $RPM_BUILD_ROOT%{_sysconfdir}/husky

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info

%files
%defattr(-,root,root)
%doc BUG-REPORTING BUGS COPYING CREDITS ChangeLog HISTORY INSTALL README TODO UPGRADE VERSION filter.pl config misc
%doc doc/{bugreport.rus,bugreport.txt,faqfmt.pl,hpt-FAQ.russian,perlwin32.rus,perlwin32.txt}
%attr(755,root,root) %{_bindir}/*
%{_infodir}/%{name}.info.bz2
%{_mandir}/*/*
%dir %{_sysconfdir}/husky
%config(noreplace) %{_sysconfdir}/husky/*

