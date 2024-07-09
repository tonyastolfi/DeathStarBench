// deprecated - needed only because we don't have the .thrift files.
#pragma once

#include <memory>

namespace apache {
namespace thrift {
namespace stdcxx {
    
template <typename T>
using shared_ptr = ::std::shared_ptr<T>;

}
}
}
