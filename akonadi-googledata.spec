Name:		akonadi-googledata
Version:	1.0.1
Summary:	Google contacts and calendar akonadi resource
Release:	%mkrel 2
License:	LGPLv2.1
Group:		Graphical desktop/KDE
URL:		http://websvn.kde.org/trunk/extragear/pim/googledata/
Source0:	http://libgcal.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	kdepimlibs4-devel
BuildRequires:	libgcal-devel
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

