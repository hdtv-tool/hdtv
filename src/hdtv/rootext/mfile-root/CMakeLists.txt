cmake_minimum_required(VERSION 3.24)

project(mfile-root LANGUAGES CXX C)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake)

include(install_setup)

find_package(ROOT REQUIRED CONFIG COMPONENTS Core Hist)

message(STATUS "ROOT Version ${ROOT_VERSION} found in ${ROOT_root_CMD}")

add_subdirectory(mfile)
add_subdirectory(matop)

add_library(${PROJECT_NAME} SHARED)

set(HEADERS MFileHist.hh MFileRoot.hh MatOp.hh VMatrix.hh)

target_sources(
    ${PROJECT_NAME}
    PRIVATE MFileHist.cc MFileRoot.cc MatOp.cc VMatrix.cc
    PUBLIC
        FILE_SET HEADERS BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR} FILES ${HEADERS}
)

target_link_libraries(${PROJECT_NAME} PRIVATE ROOT::Core ROOT::Hist matop mfile)

root_generate_dictionary(
  G__${PROJECT_NAME}
  ${HEADERS}
  MODULE
  ${PROJECT_NAME}
  LINKDEF
  LinkDef.h
)

add_library(hdtv::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_14)

install(TARGETS ${PROJECT_NAME} FILE_SET HEADERS)
