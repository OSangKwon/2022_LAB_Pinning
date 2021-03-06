#ifndef MEMORY_CLASS_H
#define MEMORY_CLASS_H

#include "champsim.h"
#include "block.h"

#include <limits>

// CACHE ACCESS TYPE
#define LOAD      0
#define RFO       1
#define PREFETCH  2
#define WRITEBACK 3
#define TRANSLATION 4
#define NUM_TYPES 5

extern uint32_t tRP,  // Row Precharge (RP) latency
                tRCD, // Row address to Column address (RCD) latency
                tCAS; // Column Address Strobe (CAS) latency

extern uint64_t l2pf_access;

// CACHE BLOCK
class BLOCK {
  public:
    bool valid = false,
         prefetch = false,
         dirty = false,
         pin = false;


    uint64_t address = 0,
             full_addr = 0,
             v_address = 0,
             full_v_addr = 0,
             data = 0,
             ip = 0,
             cpu = 0,
             instr_id = 0;


    // replacement state
    uint32_t lru = std::numeric_limits<uint32_t>::max() >> 1;
};

class MemoryRequestConsumer
{
    public:
        /*
         * add_*q() return values:
         *
         * -2 : queue full
         * -1 : packet value forwarded, returned
         * 0  : packet merged
         * >0 : new queue occupancy
         *
         */
        virtual int  add_rq(PACKET *packet) = 0;
        virtual int  add_wq(PACKET *packet) = 0;
        virtual int  add_pq(PACKET *packet) = 0;
        virtual void increment_WQ_FULL(uint64_t address) = 0;
        virtual uint32_t get_occupancy(uint8_t queue_type, uint64_t address) = 0;
        virtual uint32_t get_size(uint8_t queue_type, uint64_t address) = 0;
};

class MemoryRequestProducer
{
    public:
        MemoryRequestConsumer *lower_level;
        virtual void return_data(PACKET *packet) = 0;
    protected:
        MemoryRequestProducer() {}
        explicit MemoryRequestProducer(MemoryRequestConsumer *ll) : lower_level(ll) {}
};

// DRAM CACHE BLOCK
class DRAM_ARRAY {
  public:
    BLOCK **block;

    DRAM_ARRAY() {
        block = NULL;
    };
};

struct BANK_REQUEST {
    uint64_t cycle_available = 0,
             address = 0,
             full_addr = 0;

    uint32_t open_row = std::numeric_limits<uint32_t>::max();

    uint8_t working = 0,
            working_type = 0,
            row_buffer_hit = 0,
            drc_hit = 0,
            is_write = 0,
            is_read = 0;

    int request_index = -1;
};

#endif

