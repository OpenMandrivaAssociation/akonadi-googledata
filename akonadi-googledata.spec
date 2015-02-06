Name:		akonadi-googledata
Version:	1.2.0
Summary:	Google contacts and calendar akonadi resource
Release:	2
License:	LGPLv2.1
Group:		Graphical desktop/KDE
URL:		http://websvn.kde.org/trunk/extragear/pim/googledata/
Source0:	http://libgcal.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	kdepimlibs4-devel
BuildRequires:	libgcal-devel >= 0.9.6
BuildRequires:	boost-devel
BuildRequires:	libxslt-proc
Requires:	akonadi-kde
Obsoletes:	googledata

%description
Google contacts and calendar akonadi resource 

%files -f akonadi_gcal_resource.lang 
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_kde_bindir}/akonadi_gcal_resource
%{_kde_bindir}/akonadi_googledata_resource
%{_kde_datadir}/akonadi/agents/gcalresource.desktop
%{_kde_datadir}/akonadi/agents/googledataresource.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build
%find_lang akonadi_gcal_resource

%clean
%__rm -rf %{buildroot}



%changelog
* Wed Sep 08 2010 John Balcaen <mikala@mandriva.org> 1.2.0-1mdv2011.0
+ Revision: 576738
- Update to 1.2.0

* Mon Jul 26 2010 John Balcaen <mikala@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 560770
- Fix minimum requirement for libgcal ( >=0.9.4 )
- Update to 1.1.0

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - rebuild

* Wed Sep 30 2009 John Balcaen <mikala@mandriva.org> 1.0.1-2mdv2010.0
+ Revision: 451144
- Fix Requires

* Sat Aug 29 2009 John Balcaen <mikala@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 422209
- Update to 1.0.1
  Fix License

* Fri Aug 21 2009 John Balcaen <mikala@mandriva.org> 1.0-0.1014109.1mdv2010.0
+ Revision: 419379
- Rename to upstream name (akonadi-googledata)
  Rename spec file
  Add obsolete against googledata
- Fix upstream name (akonadi-googledata and not akonadi-google)
- Update to revision 1014109
  Fix Requires,documentation and license
  signed-off-by: neoclust@mandriva.org

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix specfile name
    - Use new upstream name

* Sun May 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0-0.969042.1mdv2010.0
+ Revision: 376665
- Fix BuildRequires
- import googledata

