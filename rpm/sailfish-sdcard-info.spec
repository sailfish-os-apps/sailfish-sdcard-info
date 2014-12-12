Summary: Sailfish SD Card Info
Name: sailfish-sdcard-info
Version: 0.0.0
Release: 1
License: LGPLv2.1
Group: System Environment/Tools
URL: https://github.com/nokius/sailfish-sdcard-info
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:  sailfishsilica-qt5
Requires: cutes-js >= 0.8
Requires: cutes >= 0.8
Requires: qt5-qtdeclarative-systeminfo
Requires: jolla-settings-system >= 0.1.69
Requires: nemo-qml-plugin-notifications-qt5
Requires: nemo-qml-plugin-systemsettings
Requires: nemo-qml-plugin-dbus-qt5
Requires:  mapplauncherd-booster-silica-qt5
BuildRequires: cmake >= 2.8
BuildRequires: qt5-default
BuildRequires: qt5-qttools
BuildRequires: qt5-qttools-linguist
Requires: sailfish-utilities-all-translations >= 0.0.1-10.1.4.jolla

%description
Get Information about your SD Card

%package ts-devel
Summary: Translation source for %{name}
%description ts-devel
Translation source for %{name}

%prep
%setup -q

%build
%cmake
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%{_datadir}/themes/jolla-ambient/meegotouch/icons/icon-m-storage.png
%{_datadir}/sailfish-sdcard-info/*.qml
%{_datadir}/jolla-settings/entries/sdcard-info.json
%{_datadir}/translations/settings-sailfish_sdcard-info_eng_en.qm


%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/settings-sailfish_sdcard-info.ts

%changelog
* Fri Dec 12 2014 Nokius
- First Build atm only Dummie wich add a Entry in the Settings
