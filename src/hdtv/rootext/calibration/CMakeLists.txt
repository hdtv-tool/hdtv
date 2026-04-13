cmake_minimum_required(VERSION 3.15 FATAL_ERROR)

project(calibration LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake)
include(install_setup)

find_package(ROOT REQUIRED CONFIG COMPONENTS Core Hist)

message(STATUS "ROOT Version ${ROOT_VERSION} found in ${ROOT_root_CMD}")

add_library(${PROJECT_NAME} SHARED)
add_library(hdtv::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(
    ${PROJECT_NAME}
    PUBLIC
        FILE_SET HEADERS
            BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}
            FILES Calibration.hpp
)

root_generate_dictionary(
  G__${PROJECT_NAME}
  Calibration.hpp
  MODULE
  ${PROJECT_NAME}
  LINKDEF
  LinkDef.h
)

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_14)
target_link_libraries(
    ${PROJECT_NAME}
    PRIVATE ROOT::Core ROOT::Hist ROOT::Graf ROOT::Gui
)

install(TARGETS ${PROJECT_NAME} FILE_SET HEADERS)
