add_executable(
    TextService
    TextService.cpp
    ${THRIFT_GEN_CPP_DIR}/TextService.cpp
    ${THRIFT_GEN_CPP_DIR}/UserMentionService.cpp
    ${THRIFT_GEN_CPP_DIR}/UrlShortenService.cpp
    ${THRIFT_GEN_CPP_DIR}/social_network_types.cpp
)

target_include_directories(
    TextService PRIVATE
    #/usr/local/include/jaegertracing
    ${THRIFT_GEN_CPP_DIR}    
)

target_link_libraries(
    TextService
    nlohmann_json::nlohmann_json
    ${THRIFT_LIB}
    ${CMAKE_THREAD_LIBS_INIT}
    ${Boost_LIBRARIES}
    Boost::log
    Boost::log_setup
    #jaegertracing
    yaml-cpp
    OpenTracing::OpenTracing
    redis++::redis++_static
)

install(TARGETS TextService DESTINATION ./)
