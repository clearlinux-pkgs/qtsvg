#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtsvg
Version  : 5.15.2
Release  : 32
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtsvg-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtsvg-everywhere-src-5.15.2.tar.xz
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
Patch1: qtsvg-stable-branch.patch

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


%package examples
Summary: examples components for the qtsvg package.
Group: Default
Requires: qtsvg-dev = %{version}-%{release}

%description examples
examples components for the qtsvg package.


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
%setup -q -n qtsvg-everywhere-src-5.15.2
cd %{_builddir}/qtsvg-everywhere-src-5.15.2
%patch1 -p1

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
export SOURCE_DATE_EPOCH=1667236971
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtsvg
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtsvg/61907422fefcd2313a9b570c31d203a6dbebd333 || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtsvg/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtsvg/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtsvg/e93757aefa405f2c9a8a55e780ae9c39542dfc3a || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtsvg/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.LGPLv21 %{buildroot}/usr/share/package-licenses/qtsvg/fe04fe44c5e1a407572a5cca79d39afd674bccf3 || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtsvg/d8b489a3c3d500a6601181e3db39bec6124b86fc || :
cp %{_builddir}/qtsvg-everywhere-src-%{version}/src/svg/XSVG_LICENSE.txt %{buildroot}/usr/share/package-licenses/qtsvg/9c7d86ef8571df996010cb73af37e99b031cd68e || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvgfont_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvggraphics_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvghandler_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvgnode_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvgstructure_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvgstyle_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qsvgtinydocument_p.h
/usr/include/qt5/QtSvg/5.15.2/QtSvg/private/qtsvgglobal_p.h
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
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QSvgIconPlugin.cmake
/usr/lib64/cmake/Qt5Gui/Qt5Gui_QSvgPlugin.cmake
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfig.cmake
/usr/lib64/cmake/Qt5Svg/Qt5SvgConfigVersion.cmake
/usr/lib64/libQt5Svg.prl
/usr/lib64/libQt5Svg.so
/usr/lib64/pkgconfig/Qt5Svg.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_svg_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/delayedencoding.pro
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/delayedencoding.qrc
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/images/drag.png
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/images/example.svg
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/main.cpp
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/mimedata.cpp
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/mimedata.h
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/sourcewidget.cpp
/usr/share/qt5/examples/svg/draganddrop/delayedencoding/sourcewidget.h
/usr/share/qt5/examples/svg/draganddrop/draganddrop.pro
/usr/share/qt5/examples/svg/embedded/desktopservices/contenttab.cpp
/usr/share/qt5/examples/svg/embedded/desktopservices/contenttab.h
/usr/share/qt5/examples/svg/embedded/desktopservices/data/Explosion.wav
/usr/share/qt5/examples/svg/embedded/desktopservices/data/designer.png
/usr/share/qt5/examples/svg/embedded/desktopservices/data/monkey_on_64x64.png
/usr/share/qt5/examples/svg/embedded/desktopservices/data/sax.mp3
/usr/share/qt5/examples/svg/embedded/desktopservices/desktopservices.pro
/usr/share/qt5/examples/svg/embedded/desktopservices/desktopservices.qrc
/usr/share/qt5/examples/svg/embedded/desktopservices/desktopwidget.cpp
/usr/share/qt5/examples/svg/embedded/desktopservices/desktopwidget.h
/usr/share/qt5/examples/svg/embedded/desktopservices/linktab.cpp
/usr/share/qt5/examples/svg/embedded/desktopservices/linktab.h
/usr/share/qt5/examples/svg/embedded/desktopservices/main.cpp
/usr/share/qt5/examples/svg/embedded/desktopservices/resources/browser.png
/usr/share/qt5/examples/svg/embedded/desktopservices/resources/heart.svg
/usr/share/qt5/examples/svg/embedded/desktopservices/resources/message.png
/usr/share/qt5/examples/svg/embedded/desktopservices/resources/music.png
/usr/share/qt5/examples/svg/embedded/desktopservices/resources/photo.png
/usr/share/qt5/examples/svg/embedded/embedded.pro
/usr/share/qt5/examples/svg/embedded/fluidlauncher/config.xml
/usr/share/qt5/examples/svg/embedded/fluidlauncher/demoapplication.cpp
/usr/share/qt5/examples/svg/embedded/fluidlauncher/demoapplication.h
/usr/share/qt5/examples/svg/embedded/fluidlauncher/fluidlauncher.cpp
/usr/share/qt5/examples/svg/embedded/fluidlauncher/fluidlauncher.h
/usr/share/qt5/examples/svg/embedded/fluidlauncher/fluidlauncher.pro
/usr/share/qt5/examples/svg/embedded/fluidlauncher/fluidlauncher.qrc
/usr/share/qt5/examples/svg/embedded/fluidlauncher/main.cpp
/usr/share/qt5/examples/svg/embedded/fluidlauncher/pictureflow.cpp
/usr/share/qt5/examples/svg/embedded/fluidlauncher/pictureflow.h
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/anomaly_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/concentriccircles.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/context2d_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/deform.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/desktopservices_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/digiflip.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/elasticnodes.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/embeddedsvgviewer.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/embeddedsvgviewer_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/flickable.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/flightinfo_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/fridgemagnets_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/ftp_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/lightmaps.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/mediaplayer.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/pathstroke.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmlcalculator.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmlclocks.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmldialcontrol.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmleasing.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmlflickr.jpg
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmlphotoviewer.jpg
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/qmltwitter.jpg
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/raycasting.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/saxbookmarks_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/softkeys_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/spectrum.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/styledemo.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/styledemo_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/weatherinfo.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/wiggly.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/screenshots/wiggly_s60.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_1.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_2.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_3.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_4.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_5.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slides/demo_6.png
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slideshow.cpp
/usr/share/qt5/examples/svg/embedded/fluidlauncher/slideshow.h
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/README.txt
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-few-clouds.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-fog.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-haze.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-icy.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-overcast.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-showers.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-sleet.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-snow.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-storm.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-sunny-very-few-clouds.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-sunny.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/icons/weather-thundershower.svg
/usr/share/qt5/examples/svg/embedded/weatherinfo/weatherinfo.cpp
/usr/share/qt5/examples/svg/embedded/weatherinfo/weatherinfo.pro
/usr/share/qt5/examples/svg/embedded/weatherinfo/weatherinfo.qrc
/usr/share/qt5/examples/svg/embeddedsvgviewer/embeddedsvgviewer.cpp
/usr/share/qt5/examples/svg/embeddedsvgviewer/embeddedsvgviewer.h
/usr/share/qt5/examples/svg/embeddedsvgviewer/embeddedsvgviewer.pro
/usr/share/qt5/examples/svg/embeddedsvgviewer/embeddedsvgviewer.qrc
/usr/share/qt5/examples/svg/embeddedsvgviewer/files/default.svg
/usr/share/qt5/examples/svg/embeddedsvgviewer/files/v-slider-handle.svg
/usr/share/qt5/examples/svg/embeddedsvgviewer/main.cpp
/usr/share/qt5/examples/svg/opengl/framebufferobject/bubbles.svg
/usr/share/qt5/examples/svg/opengl/framebufferobject/designer.png
/usr/share/qt5/examples/svg/opengl/framebufferobject/framebufferobject.pro
/usr/share/qt5/examples/svg/opengl/framebufferobject/framebufferobject.qrc
/usr/share/qt5/examples/svg/opengl/framebufferobject/glwidget.cpp
/usr/share/qt5/examples/svg/opengl/framebufferobject/glwidget.h
/usr/share/qt5/examples/svg/opengl/framebufferobject/main.cpp
/usr/share/qt5/examples/svg/opengl/opengl.pro
/usr/share/qt5/examples/svg/richtext/richtext.pro
/usr/share/qt5/examples/svg/richtext/textobject/files/heart.svg
/usr/share/qt5/examples/svg/richtext/textobject/main.cpp
/usr/share/qt5/examples/svg/richtext/textobject/resources.qrc
/usr/share/qt5/examples/svg/richtext/textobject/svgtextobject.cpp
/usr/share/qt5/examples/svg/richtext/textobject/svgtextobject.h
/usr/share/qt5/examples/svg/richtext/textobject/textobject.pro
/usr/share/qt5/examples/svg/richtext/textobject/window.cpp
/usr/share/qt5/examples/svg/richtext/textobject/window.h
/usr/share/qt5/examples/svg/svg.pro
/usr/share/qt5/examples/svg/svggenerator/displaywidget.cpp
/usr/share/qt5/examples/svg/svggenerator/displaywidget.h
/usr/share/qt5/examples/svg/svggenerator/forms/window.ui
/usr/share/qt5/examples/svg/svggenerator/main.cpp
/usr/share/qt5/examples/svg/svggenerator/resources/shapes.dat
/usr/share/qt5/examples/svg/svggenerator/svggenerator.pro
/usr/share/qt5/examples/svg/svggenerator/svggenerator.qrc
/usr/share/qt5/examples/svg/svggenerator/window.cpp
/usr/share/qt5/examples/svg/svggenerator/window.h
/usr/share/qt5/examples/svg/svgviewer/exportdialog.cpp
/usr/share/qt5/examples/svg/svgviewer/exportdialog.h
/usr/share/qt5/examples/svg/svgviewer/files/bubbles.svg
/usr/share/qt5/examples/svg/svgviewer/files/cubic.svg
/usr/share/qt5/examples/svg/svgviewer/files/spheres.svg
/usr/share/qt5/examples/svg/svgviewer/main.cpp
/usr/share/qt5/examples/svg/svgviewer/mainwindow.cpp
/usr/share/qt5/examples/svg/svgviewer/mainwindow.h
/usr/share/qt5/examples/svg/svgviewer/svgview.cpp
/usr/share/qt5/examples/svg/svgviewer/svgview.h
/usr/share/qt5/examples/svg/svgviewer/svgviewer.pro
/usr/share/qt5/examples/svg/svgviewer/svgviewer.qrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Svg.so.5
/usr/lib64/libQt5Svg.so.5.15
/usr/lib64/libQt5Svg.so.5.15.2
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
