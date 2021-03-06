FILE(GLOB JS_FILES *.js)
FILE(GLOB QML_FILES *.qml)

install(
  FILES ${JS_FILES} ${QML_FILES} ${SVG_FILES}
  DESTINATION share/${PACKAGE_NAME}
  )

add_custom_command(
    OUTPUT settings-sailfish_sdcard-info.ts
    COMMAND lupdate . -ts settings-sailfish_sdcard-info.ts
)
add_custom_target(ts_target ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/settings-sailfish_sdcard-info.ts)

add_custom_command(
    OUTPUT settings-sailfish_sdcard-info_eng_en.qm
    COMMAND lrelease -idbased settings-sailfish_sdcard-info.ts -qm settings-sailfish_sdcard-info_eng_en.qm
)
add_custom_target(qm_target ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/settings-sailfish_sdcard-info_eng_en.qm)
add_dependencies(qm_target ts_target)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/settings-sailfish_sdcard-info.ts DESTINATION share/translations/source)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/settings-sailfish_sdcard-info_eng_en.qm DESTINATION share/translations)

