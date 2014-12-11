PROJECT(SAILFISH_SDCARD-INFO)
cmake_minimum_required(VERSION 2.8)

set(prefix ${CMAKE_INSTALL_PREFIX})

set(PACKAGE_NAME sailfish-sdcard-info)
set(DEPLOYMENT_PATH ${prefix}/share/${PACKAGE_NAME})

configure_file(sdcard-info.json.in sdcard-info.json @ONLY)
install(FILES sdcard-info.json DESTINATION share/jolla-settings/entries)

add_subdirectory(qml)
