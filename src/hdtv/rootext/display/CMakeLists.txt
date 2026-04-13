cmake_minimum_required(VERSION 3.15 FATAL_ERROR)

project(display LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake)
include(install_setup)

set(HEADERS
    DisplayBlock.hh
    DisplayCut.hh
    DisplayFunc.hh
    DisplayObj.hh
    DisplayObjZIndex.hh
    DisplaySpec.hh
    DisplayStack.hh
    Marker.hh
    MTViewer.hh
    Painter.hh
    View1D.hh
    View2D.hh
    Viewer.hh
    View.hh
    XMarker.hh
    YMarker.hh
)

find_package(X11 REQUIRED)
find_package(ROOT REQUIRED CONFIG COMPONENTS Core Hist Graf Gui)
message(STATUS "ROOT Version ${ROOT_VERSION} found in ${ROOT_root_CMD}")

add_library(${PROJECT_NAME} SHARED)
add_library(hdtv::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(
    ${PROJECT_NAME}
    PRIVATE
        DisplayBlock.cc
        DisplayCut.cc
        DisplayFunc.cc
        DisplayObj.cc
        DisplaySpec.cc
        DisplayStack.cc
        Marker.cc
        MTViewer.cc
        Painter.cc
        View1D.cc
        View2D.cc
        View.cc
        Viewer.cc
        XMarker.cc
        YMarker.cc
    PUBLIC
        FILE_SET HEADERS BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} FILES ${HEADERS}
)

# HACK: Should link to calibration via find_package instead.
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../calibration)

root_generate_dictionary(G__${PROJECT_NAME} ${HEADERS} MODULE ${PROJECT_NAME} LINKDEF LinkDef.h)

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_14)

target_link_libraries(
    ${PROJECT_NAME}
    PRIVATE ROOT::Core ROOT::Hist ROOT::Graf ROOT::Gui X11
)

install(TARGETS ${PROJECT_NAME} FILE_SET HEADERS)
