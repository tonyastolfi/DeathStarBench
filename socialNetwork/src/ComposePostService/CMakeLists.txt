message("ComposePostService: THRIFT_GEN_CPP_DIR is ${THRIFT_GEN_CPP_DIR}")

add_executable(
    ComposePostService
    ComposePostService.cpp
    ${THRIFT_GEN_CPP_DIR}/ComposePostService.cpp
    ${THRIFT_GEN_CPP_DIR}/PostStorageService.cpp
    ${THRIFT_GEN_CPP_DIR}/UserTimelineService.cpp
    ${THRIFT_GEN_CPP_DIR}/UserService.cpp
    ${THRIFT_GEN_CPP_DIR}/UniqueIdService.cpp
    ${THRIFT_GEN_CPP_DIR}/MediaService.cpp
    ${THRIFT_GEN_CPP_DIR}/TextService.cpp
    ${THRIFT_GEN_CPP_DIR}/HomeTimelineService.cpp
    ${THRIFT_GEN_CPP_DIR}/social_network_types.cpp
)

target_include_directories(
    ComposePostService PRIVATE
    /usr/local/include/jaegertracing
    ${THRIFT_GEN_CPP_DIR}
)

target_link_libraries(
    ComposePostService
    ${THRIFT_LIB}
    ${CMAKE_THREAD_LIBS_INIT}
    ${Boost_LIBRARIES}
    nlohmann_json::nlohmann_json
    Boost::log
    Boost::log_setup
    OpenSSL::SSL
    /usr/local/lib/libjaegertracing.so
    /usr/local/lib/libSimpleAmqpClient.so
    yaml-cpp
    OpenTracing::OpenTracing
    redis++::redis++_static
)

install(TARGETS ComposePostService DESTINATION ./)
