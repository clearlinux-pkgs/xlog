#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1903030B4FDDF9A0 (andystewart@comcast.net)
#
Name     : xlog
Version  : 2.0.22
Release  : 14
URL      : https://download.savannah.nongnu.org/releases/xlog/xlog-2.0.22.tar.gz
Source0  : https://download.savannah.nongnu.org/releases/xlog/xlog-2.0.22.tar.gz
Source1  : https://download.savannah.nongnu.org/releases/xlog/xlog-2.0.22.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: xlog-bin = %{version}-%{release}
Requires: xlog-data = %{version}-%{release}
Requires: xlog-license = %{version}-%{release}
Requires: xlog-locales = %{version}-%{release}
Requires: xlog-man = %{version}-%{release}
BuildRequires : desktop-file-utils
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(hamlib)

%description
- REQUIREMENTS -
----------------
See the INSTALL file for package requirements when you want to compile xlog
yourself.

%package bin
Summary: bin components for the xlog package.
Group: Binaries
Requires: xlog-data = %{version}-%{release}
Requires: xlog-license = %{version}-%{release}

%description bin
bin components for the xlog package.


%package data
Summary: data components for the xlog package.
Group: Data

%description data
data components for the xlog package.


%package doc
Summary: doc components for the xlog package.
Group: Documentation
Requires: xlog-man = %{version}-%{release}

%description doc
doc components for the xlog package.


%package license
Summary: license components for the xlog package.
Group: Default

%description license
license components for the xlog package.


%package locales
Summary: locales components for the xlog package.
Group: Default

%description locales
locales components for the xlog package.


%package man
Summary: man components for the xlog package.
Group: Default

%description man
man components for the xlog package.


%prep
%setup -q -n xlog-2.0.22
cd %{_builddir}/xlog-2.0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614617489
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1614617489
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xlog
cp %{_builddir}/xlog-2.0.22/COPYING %{buildroot}/usr/share/package-licenses/xlog/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
cp %{_builddir}/xlog-2.0.22/data/doc/manual/license.dox %{buildroot}/usr/share/package-licenses/xlog/b38b0c6cc916b2162c027d074710f8dfb1411711
cp %{_builddir}/xlog-2.0.22/data/doc/manual/output/html/license.html %{buildroot}/usr/share/package-licenses/xlog/b2eeff27106b7c09693886cfa0aa14980c04ed47
%make_install
%find_lang xlog
## Remove excluded files
rm -f %{buildroot}/usr/share/applications/mimeinfo.cache

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xlog

%files data
%defattr(-,root,root,-)
/usr/share/applications/xlog.desktop
/usr/share/icons/gnome-mime-text-x-xlog.png
/usr/share/icons/xlog-icon.png
/usr/share/mime-packages/xlog.xml
/usr/share/pixmaps/xlog/countrymap.png
/usr/share/pixmaps/xlog/cwdaemon.png
/usr/share/pixmaps/xlog/gnome-mime-text-x-xlog.png
/usr/share/pixmaps/xlog/jigsaw.png
/usr/share/pixmaps/xlog/mini-clock.xpm
/usr/share/pixmaps/xlog/mini-trx.xpm
/usr/share/pixmaps/xlog/mini-xlog.xpm
/usr/share/pixmaps/xlog/s-meter.xpm
/usr/share/pixmaps/xlog/s.xpm
/usr/share/pixmaps/xlog/s0.xpm
/usr/share/pixmaps/xlog/s1.xpm
/usr/share/pixmaps/xlog/s2.xpm
/usr/share/pixmaps/xlog/s3.xpm
/usr/share/pixmaps/xlog/s4.xpm
/usr/share/pixmaps/xlog/s5.xpm
/usr/share/pixmaps/xlog/s6.xpm
/usr/share/pixmaps/xlog/s7.xpm
/usr/share/pixmaps/xlog/s8.xpm
/usr/share/pixmaps/xlog/s9.xpm
/usr/share/pixmaps/xlog/xlog-b4.png
/usr/share/pixmaps/xlog/xlog-icon.png
/usr/share/pixmaps/xlog/xlog-keyer.png
/usr/share/pixmaps/xlog/xlog-map.png
/usr/share/pixmaps/xlog/xlog-scoring.png
/usr/share/pixmaps/xlog/xlog.png
/usr/share/pixmaps/xlog/xlog.svg
/usr/share/pixmaps/xlog/xlog.xpm
/usr/share/xlog/dxcc/area.dat
/usr/share/xlog/dxcc/cty.dat
/usr/share/xlog/maps/1S.png
/usr/share/xlog/maps/3A.png
/usr/share/xlog/maps/3B6.png
/usr/share/xlog/maps/3B8.png
/usr/share/xlog/maps/3B9.png
/usr/share/xlog/maps/3C.png
/usr/share/xlog/maps/3C0.png
/usr/share/xlog/maps/3D2.png
/usr/share/xlog/maps/3D2/c.png
/usr/share/xlog/maps/3D2/r.png
/usr/share/xlog/maps/3DA.png
/usr/share/xlog/maps/3V.png
/usr/share/xlog/maps/3W.png
/usr/share/xlog/maps/3X.png
/usr/share/xlog/maps/3Y/b.png
/usr/share/xlog/maps/3Y/p.png
/usr/share/xlog/maps/4J.png
/usr/share/xlog/maps/4L.png
/usr/share/xlog/maps/4O.png
/usr/share/xlog/maps/4S.png
/usr/share/xlog/maps/4U1I.png
/usr/share/xlog/maps/4U1U.png
/usr/share/xlog/maps/4W.png
/usr/share/xlog/maps/4X.png
/usr/share/xlog/maps/5A.png
/usr/share/xlog/maps/5B.png
/usr/share/xlog/maps/5H.png
/usr/share/xlog/maps/5N.png
/usr/share/xlog/maps/5R.png
/usr/share/xlog/maps/5T.png
/usr/share/xlog/maps/5U.png
/usr/share/xlog/maps/5V.png
/usr/share/xlog/maps/5W.png
/usr/share/xlog/maps/5X.png
/usr/share/xlog/maps/5Z.png
/usr/share/xlog/maps/6W.png
/usr/share/xlog/maps/6Y.png
/usr/share/xlog/maps/7O.png
/usr/share/xlog/maps/7P.png
/usr/share/xlog/maps/7Q.png
/usr/share/xlog/maps/7X.png
/usr/share/xlog/maps/8P.png
/usr/share/xlog/maps/8Q.png
/usr/share/xlog/maps/8R.png
/usr/share/xlog/maps/9A.png
/usr/share/xlog/maps/9G.png
/usr/share/xlog/maps/9H.png
/usr/share/xlog/maps/9J.png
/usr/share/xlog/maps/9K.png
/usr/share/xlog/maps/9L.png
/usr/share/xlog/maps/9M2.png
/usr/share/xlog/maps/9M6.png
/usr/share/xlog/maps/9N.png
/usr/share/xlog/maps/9Q.png
/usr/share/xlog/maps/9U.png
/usr/share/xlog/maps/9V.png
/usr/share/xlog/maps/9X.png
/usr/share/xlog/maps/9Y.png
/usr/share/xlog/maps/A2.png
/usr/share/xlog/maps/A3.png
/usr/share/xlog/maps/A4.png
/usr/share/xlog/maps/A5.png
/usr/share/xlog/maps/A6.png
/usr/share/xlog/maps/A7.png
/usr/share/xlog/maps/A9.png
/usr/share/xlog/maps/AP.png
/usr/share/xlog/maps/BS7.png
/usr/share/xlog/maps/BV.png
/usr/share/xlog/maps/BV9P.png
/usr/share/xlog/maps/BY.png
/usr/share/xlog/maps/C2.png
/usr/share/xlog/maps/C3.png
/usr/share/xlog/maps/C5.png
/usr/share/xlog/maps/C6.png
/usr/share/xlog/maps/C9.png
/usr/share/xlog/maps/CE.png
/usr/share/xlog/maps/CE0X.png
/usr/share/xlog/maps/CE0Y.png
/usr/share/xlog/maps/CE0Z.png
/usr/share/xlog/maps/CE9.png
/usr/share/xlog/maps/CM.png
/usr/share/xlog/maps/CN.png
/usr/share/xlog/maps/CP.png
/usr/share/xlog/maps/CT.png
/usr/share/xlog/maps/CT3.png
/usr/share/xlog/maps/CU.png
/usr/share/xlog/maps/CX.png
/usr/share/xlog/maps/CY0.png
/usr/share/xlog/maps/CY9.png
/usr/share/xlog/maps/D2.png
/usr/share/xlog/maps/D4.png
/usr/share/xlog/maps/D6.png
/usr/share/xlog/maps/DL.png
/usr/share/xlog/maps/DU.png
/usr/share/xlog/maps/E3.png
/usr/share/xlog/maps/E4.png
/usr/share/xlog/maps/E5/n.png
/usr/share/xlog/maps/E5/s.png
/usr/share/xlog/maps/E7.png
/usr/share/xlog/maps/EA.png
/usr/share/xlog/maps/EA6.png
/usr/share/xlog/maps/EA8.png
/usr/share/xlog/maps/EA9.png
/usr/share/xlog/maps/EI.png
/usr/share/xlog/maps/EK.png
/usr/share/xlog/maps/EL.png
/usr/share/xlog/maps/EP.png
/usr/share/xlog/maps/ER.png
/usr/share/xlog/maps/ES.png
/usr/share/xlog/maps/ET.png
/usr/share/xlog/maps/EU.png
/usr/share/xlog/maps/EX.png
/usr/share/xlog/maps/EY.png
/usr/share/xlog/maps/EZ.png
/usr/share/xlog/maps/F.png
/usr/share/xlog/maps/FG.png
/usr/share/xlog/maps/FH.png
/usr/share/xlog/maps/FJ.png
/usr/share/xlog/maps/FK.png
/usr/share/xlog/maps/FK/c.png
/usr/share/xlog/maps/FM.png
/usr/share/xlog/maps/FO.png
/usr/share/xlog/maps/FO/a.png
/usr/share/xlog/maps/FO/c.png
/usr/share/xlog/maps/FO/m.png
/usr/share/xlog/maps/FP.png
/usr/share/xlog/maps/FR.png
/usr/share/xlog/maps/FR/g.png
/usr/share/xlog/maps/FR/j.png
/usr/share/xlog/maps/FR/t.png
/usr/share/xlog/maps/FS.png
/usr/share/xlog/maps/FT5W.png
/usr/share/xlog/maps/FT5X.png
/usr/share/xlog/maps/FT5Z.png
/usr/share/xlog/maps/FW.png
/usr/share/xlog/maps/FY.png
/usr/share/xlog/maps/G.png
/usr/share/xlog/maps/GD.png
/usr/share/xlog/maps/GI.png
/usr/share/xlog/maps/GJ.png
/usr/share/xlog/maps/GM.png
/usr/share/xlog/maps/GU.png
/usr/share/xlog/maps/GW.png
/usr/share/xlog/maps/H4.png
/usr/share/xlog/maps/H40.png
/usr/share/xlog/maps/HA.png
/usr/share/xlog/maps/HB.png
/usr/share/xlog/maps/HB0.png
/usr/share/xlog/maps/HC.png
/usr/share/xlog/maps/HC8.png
/usr/share/xlog/maps/HH.png
/usr/share/xlog/maps/HI.png
/usr/share/xlog/maps/HK.png
/usr/share/xlog/maps/HK0/a.png
/usr/share/xlog/maps/HK0/m.png
/usr/share/xlog/maps/HL.png
/usr/share/xlog/maps/HM.png
/usr/share/xlog/maps/HP.png
/usr/share/xlog/maps/HR.png
/usr/share/xlog/maps/HS.png
/usr/share/xlog/maps/HV.png
/usr/share/xlog/maps/HZ.png
/usr/share/xlog/maps/I.png
/usr/share/xlog/maps/IS.png
/usr/share/xlog/maps/J2.png
/usr/share/xlog/maps/J3.png
/usr/share/xlog/maps/J5.png
/usr/share/xlog/maps/J6.png
/usr/share/xlog/maps/J7.png
/usr/share/xlog/maps/J8.png
/usr/share/xlog/maps/JA.png
/usr/share/xlog/maps/JD/m.png
/usr/share/xlog/maps/JD/o.png
/usr/share/xlog/maps/JT.png
/usr/share/xlog/maps/JW.png
/usr/share/xlog/maps/JX.png
/usr/share/xlog/maps/JY.png
/usr/share/xlog/maps/K.png
/usr/share/xlog/maps/KG4.png
/usr/share/xlog/maps/KH0.png
/usr/share/xlog/maps/KH1.png
/usr/share/xlog/maps/KH2.png
/usr/share/xlog/maps/KH3.png
/usr/share/xlog/maps/KH4.png
/usr/share/xlog/maps/KH5.png
/usr/share/xlog/maps/KH5K.png
/usr/share/xlog/maps/KH6.png
/usr/share/xlog/maps/KH7K.png
/usr/share/xlog/maps/KH8.png
/usr/share/xlog/maps/KH8/s.png
/usr/share/xlog/maps/KH9.png
/usr/share/xlog/maps/KL.png
/usr/share/xlog/maps/KP1.png
/usr/share/xlog/maps/KP2.png
/usr/share/xlog/maps/KP4.png
/usr/share/xlog/maps/KP5.png
/usr/share/xlog/maps/LA.png
/usr/share/xlog/maps/LU.png
/usr/share/xlog/maps/LX.png
/usr/share/xlog/maps/LY.png
/usr/share/xlog/maps/LZ.png
/usr/share/xlog/maps/OA.png
/usr/share/xlog/maps/OD.png
/usr/share/xlog/maps/OE.png
/usr/share/xlog/maps/OH.png
/usr/share/xlog/maps/OH0.png
/usr/share/xlog/maps/OJ0.png
/usr/share/xlog/maps/OK.png
/usr/share/xlog/maps/OM.png
/usr/share/xlog/maps/ON.png
/usr/share/xlog/maps/OX.png
/usr/share/xlog/maps/OY.png
/usr/share/xlog/maps/OZ.png
/usr/share/xlog/maps/P2.png
/usr/share/xlog/maps/P4.png
/usr/share/xlog/maps/PA.png
/usr/share/xlog/maps/PJ2.png
/usr/share/xlog/maps/PJ7.png
/usr/share/xlog/maps/PY.png
/usr/share/xlog/maps/PY0F.png
/usr/share/xlog/maps/PY0S.png
/usr/share/xlog/maps/PY0T.png
/usr/share/xlog/maps/PZ.png
/usr/share/xlog/maps/R1FJ.png
/usr/share/xlog/maps/R1MV.png
/usr/share/xlog/maps/S0.png
/usr/share/xlog/maps/S2.png
/usr/share/xlog/maps/S5.png
/usr/share/xlog/maps/S7.png
/usr/share/xlog/maps/S9.png
/usr/share/xlog/maps/SM.png
/usr/share/xlog/maps/SP.png
/usr/share/xlog/maps/ST.png
/usr/share/xlog/maps/SU.png
/usr/share/xlog/maps/SV.png
/usr/share/xlog/maps/SV/a.png
/usr/share/xlog/maps/SV5.png
/usr/share/xlog/maps/SV9.png
/usr/share/xlog/maps/T2.png
/usr/share/xlog/maps/T30.png
/usr/share/xlog/maps/T31.png
/usr/share/xlog/maps/T32.png
/usr/share/xlog/maps/T33.png
/usr/share/xlog/maps/T5.png
/usr/share/xlog/maps/T7.png
/usr/share/xlog/maps/T8.png
/usr/share/xlog/maps/TA.png
/usr/share/xlog/maps/TF.png
/usr/share/xlog/maps/TG.png
/usr/share/xlog/maps/TI.png
/usr/share/xlog/maps/TI9.png
/usr/share/xlog/maps/TJ.png
/usr/share/xlog/maps/TK.png
/usr/share/xlog/maps/TL.png
/usr/share/xlog/maps/TN.png
/usr/share/xlog/maps/TR.png
/usr/share/xlog/maps/TT.png
/usr/share/xlog/maps/TU.png
/usr/share/xlog/maps/TY.png
/usr/share/xlog/maps/TZ.png
/usr/share/xlog/maps/UA.png
/usr/share/xlog/maps/UA2.png
/usr/share/xlog/maps/UA9.png
/usr/share/xlog/maps/UK.png
/usr/share/xlog/maps/UN.png
/usr/share/xlog/maps/UR.png
/usr/share/xlog/maps/V2.png
/usr/share/xlog/maps/V3.png
/usr/share/xlog/maps/V4.png
/usr/share/xlog/maps/V5.png
/usr/share/xlog/maps/V6.png
/usr/share/xlog/maps/V7.png
/usr/share/xlog/maps/V8.png
/usr/share/xlog/maps/VE.png
/usr/share/xlog/maps/VK.png
/usr/share/xlog/maps/VK0H.png
/usr/share/xlog/maps/VK0M.png
/usr/share/xlog/maps/VK9C.png
/usr/share/xlog/maps/VK9L.png
/usr/share/xlog/maps/VK9M.png
/usr/share/xlog/maps/VK9N.png
/usr/share/xlog/maps/VK9W.png
/usr/share/xlog/maps/VK9X.png
/usr/share/xlog/maps/VP2E.png
/usr/share/xlog/maps/VP2M.png
/usr/share/xlog/maps/VP2V.png
/usr/share/xlog/maps/VP5.png
/usr/share/xlog/maps/VP6.png
/usr/share/xlog/maps/VP6/d.png
/usr/share/xlog/maps/VP8.png
/usr/share/xlog/maps/VP8/g.png
/usr/share/xlog/maps/VP8/h.png
/usr/share/xlog/maps/VP8/o.png
/usr/share/xlog/maps/VP8/s.png
/usr/share/xlog/maps/VP9.png
/usr/share/xlog/maps/VQ9.png
/usr/share/xlog/maps/VR.png
/usr/share/xlog/maps/VU.png
/usr/share/xlog/maps/VU4.png
/usr/share/xlog/maps/VU7.png
/usr/share/xlog/maps/XE.png
/usr/share/xlog/maps/XF4.png
/usr/share/xlog/maps/XT.png
/usr/share/xlog/maps/XU.png
/usr/share/xlog/maps/XW.png
/usr/share/xlog/maps/XX9.png
/usr/share/xlog/maps/XZ.png
/usr/share/xlog/maps/YA.png
/usr/share/xlog/maps/YB.png
/usr/share/xlog/maps/YI.png
/usr/share/xlog/maps/YJ.png
/usr/share/xlog/maps/YK.png
/usr/share/xlog/maps/YL.png
/usr/share/xlog/maps/YN.png
/usr/share/xlog/maps/YO.png
/usr/share/xlog/maps/YS.png
/usr/share/xlog/maps/YU.png
/usr/share/xlog/maps/YV.png
/usr/share/xlog/maps/YV0.png
/usr/share/xlog/maps/Z2.png
/usr/share/xlog/maps/Z3.png
/usr/share/xlog/maps/ZA.png
/usr/share/xlog/maps/ZB.png
/usr/share/xlog/maps/ZC4.png
/usr/share/xlog/maps/ZD7.png
/usr/share/xlog/maps/ZD8.png
/usr/share/xlog/maps/ZD9.png
/usr/share/xlog/maps/ZF.png
/usr/share/xlog/maps/ZK2.png
/usr/share/xlog/maps/ZK3.png
/usr/share/xlog/maps/ZL.png
/usr/share/xlog/maps/ZL7.png
/usr/share/xlog/maps/ZL8.png
/usr/share/xlog/maps/ZL9.png
/usr/share/xlog/maps/ZP.png
/usr/share/xlog/maps/ZS.png
/usr/share/xlog/maps/ZS8.png
/usr/share/xlog/maps/worldmap.jpg

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xlog/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xlog/a6adc13d0c809ab8cb68e6e3b6eb7571bd0e2920
/usr/share/package-licenses/xlog/b2eeff27106b7c09693886cfa0aa14980c04ed47
/usr/share/package-licenses/xlog/b38b0c6cc916b2162c027d074710f8dfb1411711

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xlog.1

%files locales -f xlog.lang
%defattr(-,root,root,-)

