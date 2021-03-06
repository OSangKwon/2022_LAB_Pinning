#ifndef UTIL_H
#define UTIL_H

#include <cstdint>

constexpr unsigned lg2(uint64_t n)
{
    return n < 2 ? 0 : 1+lg2(n/2);
}

constexpr uint64_t bitmask(std::size_t begin, std::size_t end = 0)
{
    return ((1ull << (begin - end))-1) << end;
}

constexpr uint64_t splice_bits(uint64_t upper, uint64_t lower, std::size_t bits)
{
    return (upper & ~bitmask(bits)) | (lower & bitmask(bits));
}

template <typename T>
struct is_valid
{
    using argument_type = T;
    is_valid() {}
    bool operator()(const argument_type &test)
    {
        return test.valid;
    }
};

template <typename T>
struct is_pin
{
    using argument_type = T;
    is_pin() {}
    bool operator()(const argument_type &test)
    {
        return test.pin;
    }
};

template <typename T>
struct eq_addr
{
    using argument_type = T;
    const decltype(argument_type::address) val;
    const std::size_t shamt = 0;

    explicit eq_addr(decltype(argument_type::address) val) : val(val) {}
    eq_addr(decltype(argument_type::address) val, std::size_t shamt) : val(val), shamt(shamt) {}

    bool operator()(const argument_type &test)
    {
        is_valid<argument_type> validtest;
        return validtest(test) && (test.address >> shamt) == (val >> shamt);
    }
};

/*
 * A comparator to determine the LRU element. To use this comparator, the type must have a member
 * variable named "lru" and have a specialization of is_valid<>.
 *
 * To use:
 *     auto lru_elem = std::max_element(std::begin(set), std::end(set), lru_comparator<BLOCK>());
 *
 * The MRU element can be found using std::min_element instead.
 */
template <typename T, typename U = T>
struct lru_comparator
{
    using first_argument_type = T;
    using second_argument_type = U;
    bool operator()(const first_argument_type &lhs, const second_argument_type &rhs)
    {
        is_valid<first_argument_type> first_validtest;
        is_valid<second_argument_type> second_validtest;
        //is_pin<first_argument_type> first_pintest;
        //is_pin<second_argument_type> second_pintest;
        //return !second_pintest(rhs)|| !second_validtest(rhs) || ((first_pintest(lhs) && (first_validtest(lhs))) && lhs.lru < rhs.lru);
        return !second_validtest(rhs) || (first_validtest(lhs) && lhs.lru < rhs.lru);
    }
};

/*
template <typename T, typename U = T>
struct dead_comparator
{
    using first_argument_type = T;
    using second_argument_type = U;
    bool operator()(const first_argument_type &lhs, const second_argument_type &rhs)
    {
        is_valid<first_argument_type> first_validtest;
        is_valid<second_argument_type> second_validtest;
        return !second_validtest(rhs) || (first_validtest(lhs) && lhs.access_bit > rhs.access_bit);
    }
};
*/

/*
 * A functor to reorder elements to a new LRU order.
 * The type must have a member variable named "lru".
 *
 * To use:
 *     std::for_each(std::begin(set), std::end(set), lru_updater<BLOCK>(hit_element));
 */
template <typename T>
struct lru_updater
{
    const decltype(T::lru) val;
    explicit lru_updater(decltype(T::lru) val) : val(val) {}

    template <typename U>
    explicit lru_updater(U iter) : val(iter->lru) {}

    void operator()(T &x)
    {
        if (x.lru == val) x.lru = 0;
        else ++x.lru;
    }
};

template <typename T, typename U=T>
struct ord_event_cycle
{
    using first_argument_type = T;
    using second_argument_type = U;
    bool operator() (const first_argument_type &lhs, const second_argument_type &rhs)
    {
        is_valid<first_argument_type> first_validtest;
        is_valid<second_argument_type> second_validtest;
        return !second_validtest(rhs) || (first_validtest(lhs) && lhs.event_cycle < rhs.event_cycle);
    }
};

#endif

