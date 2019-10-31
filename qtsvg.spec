#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtsvg
Version  : 5.13.2
Release  : 18
URL      : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtsvg-everywhere-src-5.13.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.13/5.13.2/submodules/qtsvg-everywhere-src-5.13.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: qtsvg-lib = %{version}-%{release}
Requires: qtsvg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
The scalable icons are from:
http://tango.freedesktop.org/Tango_Icon_Library
http://darkobra.deviantart.com/art/Tango-Weather-Icon-Pack-98024429

%package dev
Summary: dev components for the qtsvg package.
Group: Development
Requires: qtsvg-lib = %{version}-%{release}
Provides: qtsvg-devel = %{version}-%{release}
Requires: qtsvg = %{version}-%{release}

%description dev
dev components for the qtsvg package.


%package lib
Summary: lib components for the qtsvg package.
Group: Libraries
Requires: qtsvg-license = %{version}-%{release}

%description lib
lib components for the qtsvg package.


%package license
Summary: license components for the qtsvg package.
Group: Default

%description license
license components for the qtsvg package.


%prep
%setup -q -n qtsvg-everywhere-src-5.13.2
cd %{_builddir}/qtsvg-everywhere-src-5.13.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1572500657
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtsvg
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtsvg/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtsvg/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtsvg/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtsvg/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtsvg/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.LGPLv21 %{buildroot}/usr/share/package-licenses/qtsvg/fe04fe44c5e1a407572a5cca79d39afd674bccf3
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/d8b489a3c3d500a6601181e3db39bec6124b86fc
cp %{_builddir}/qtsvg-everywhere-src-5.13.2/src/svg/XSVG_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtsvg/9c7d86ef8571df996010cb73af37e99b031cd68e
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvgfont_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvggraphics_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvghandler_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvgnode_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvgstructure_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvgstyle_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qsvgtinydocument_p.h
/usr/include/qt5/QtSvg/5.13.2/QtSvg/private/qtsvgglobal_p.h
/usr/include/qt5/QtSvg/QGraphicsSvgItem
/usr/include/qt5/QtSvg/QSvgGenerator
/usr/include/qt5/QtSvg/QSvgRenderer
/usr/include/qt5/QtSvg/QSvgWidget
/usr/include/qt5/QtSvg/QtSvg
/usr/include/qt5/QtSvg/QtSvgDepends
/usr/include/qt5/QtSvg/QtSvgVersion
/usr/include/qt5/QtSvg/qgraphicssvgitem.h
/usr/include/qt5/QtSvg/qsvggenerator.h
/usr/include/qt5/QtSvg/qsvgrenderer.h
/usr/include/qt5/QtSvg/qsvgwidget.h
/usr/include/qt5/QtSvg/qtsvgglobal.h
/usr/include/qt5/QtSvg/qtsvgversion.h
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfig.cmake
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfigVersion.cmake
/usr/lib64/cmake/Qt5Svg/Qt5Svg_QSvgIconPlugin.cmake
/usr/lib64/cmake/Qt5Svg/Qt5Svg_QSvgPlugin.cmake
/usr/lib64/libQt5Svg.prl
/usr/lib64/libQt5Svg.so
/usr/lib64/pkgconfig/Qt5Svg.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Svg.so.5
/usr/lib64/libQt5Svg.so.5.13
/usr/lib64/libQt5Svg.so.5.13.2
/usr/lib64/qt5/plugins/iconengines/libqsvgicon.so
/usr/lib64/qt5/plugins/imageformats/libqsvg.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtsvg/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtsvg/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtsvg/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
/usr/share/package-licenses/qtsvg/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtsvg/9c7d86ef8571df996010cb73af37e99b031cd68e
/usr/share/package-licenses/qtsvg/d8b489a3c3d500a6601181e3db39bec6124b86fc
/usr/share/package-licenses/qtsvg/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtsvg/f45ee1c765646813b442ca58de72e20a64a7ddba
/usr/share/package-licenses/qtsvg/fe04fe44c5e1a407572a5cca79d39afd674bccf3
