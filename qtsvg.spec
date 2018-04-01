#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtsvg
Version  : 5.10.1
Release  : 2
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtsvg-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtsvg-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: qtsvg-lib
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(zlib)
BuildRequires : qtbase-dev
BuildRequires : zlib-dev

%description
This directory contains autotests and benchmarks based on QTestlib. In order
to run the autotests reliably, you need to configure a desktop to match the
test environment that these tests are written for.

%package dev
Summary: dev components for the qtsvg package.
Group: Development
Requires: qtsvg-lib
Provides: qtsvg-devel

%description dev
dev components for the qtsvg package.


%package lib
Summary: lib components for the qtsvg package.
Group: Libraries

%description lib
lib components for the qtsvg package.


%prep
%setup -q -n qtsvg-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvgfont_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvggraphics_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvghandler_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvgnode_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvgstructure_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvgstyle_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qsvgtinydocument_p.h
/usr/include/qt5/QtSvg/5.10.1/QtSvg/private/qtsvgglobal_p.h
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
/usr/lib64/libQt5Svg.la
/usr/lib64/libQt5Svg.prl
/usr/lib64/libQt5Svg.so
/usr/lib64/pkgconfig/Qt5Svg.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Svg.so.5
/usr/lib64/libQt5Svg.so.5.10
/usr/lib64/libQt5Svg.so.5.10.1
/usr/lib64/qt5/plugins/iconengines/libqsvgicon.so
/usr/lib64/qt5/plugins/imageformats/libqsvg.so
