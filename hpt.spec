%define fver	1.4

%define pre	rc5
%define rel	2
%define release	0.%{pre}.%{rel}

Summary:	Highly Portable FTN Message Tosser
Name:           hpt
Version:        1.4.0
Release:        %mkrel 0.%{pre}.%{rel}
License:	GPLv2+
Group:		Networking/Other
Source:		http://downloads.sourceforge.net/husky/%{name}-%{fver}-%{pre}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Patch0:		hpt-20021015-main.patch
Patch1:		hpt-20021015-doc.patch
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
%patch0 -p1
%patch1 -p1

%build
%make OPTCFLAGS=" -s -c -fPIC %{optflags}"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
make BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} install
make INFODIR=%{buildroot}%{_infodir} -C doc install
rm -rf %{buildroot}%{_infodir}/dir
install -d %{buildroot}%{_sysconfdir}/husky
install -m 644 config/{config,path,links,areas,packer} %{buildroot}%{_sysconfdir}/husky

%clean
rm -rf %{buildroot}

%post
%_install_info %{name}.info

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

