CC := gcc
CXX := g++
CFLAGS := -Wall -std=gnu99 -g
CXXFLAGS := -Wall -std=c++17 -g
CPPFLAGS :=  -Iinc -MMD -MP -g
LDFLAGS := 
LDLIBS := 

.phony: all clean

all: bin/champsim

clean: 
	 find . -name \*.o -delete
	 find . -name \*.d -delete
	 $(RM) -r obj
	 find prefetcher/no_l1i -name \*.o -delete
	 find prefetcher/no_l1i -name \*.d -delete
	 find prefetcher/next_line_l1d -name \*.o -delete
	 find prefetcher/next_line_l1d -name \*.d -delete
	 find prefetcher/next_line_l2c -name \*.o -delete
	 find prefetcher/next_line_l2c -name \*.d -delete
	 find branch/bimodal -name \*.o -delete
	 find branch/bimodal -name \*.d -delete
	 find btb/basic_btb -name \*.o -delete
	 find btb/basic_btb -name \*.d -delete
	 find prefetcher/next_line_llc -name \*.o -delete
	 find prefetcher/next_line_llc -name \*.d -delete
	 find replacement/lru_llc -name \*.o -delete
	 find replacement/lru_llc -name \*.d -delete

bin/champsim: $(patsubst %.cc,%.o,$(wildcard src/*.cc)) obj/cpu0l1iprefetcher.a obj/cpu0l1dprefetcher.a obj/cpu0l2cprefetcher.a obj/cpu0branch_predictor.a obj/cpu0btb.a obj/cpu0llprefetcher.a obj/cpu0llreplacement.a
	$(CXX) $(LDFLAGS) -o $@ $^ $(LDLIBS)

prefetcher/no_l1i/%.o: CFLAGS += -Iprefetcher/no_l1i
prefetcher/no_l1i/%.o: CXXFLAGS += -Iprefetcher/no_l1i
obj/cpu0l1iprefetcher.a: $(patsubst %.cc,%.o,$(wildcard prefetcher/no_l1i/*.cc)) $(patsubst %.c,%.o,$(wildcard prefetcher/no_l1i/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

prefetcher/next_line_l1d/%.o: CFLAGS += -Iprefetcher/next_line_l1d
prefetcher/next_line_l1d/%.o: CXXFLAGS += -Iprefetcher/next_line_l1d
obj/cpu0l1dprefetcher.a: $(patsubst %.cc,%.o,$(wildcard prefetcher/next_line_l1d/*.cc)) $(patsubst %.c,%.o,$(wildcard prefetcher/next_line_l1d/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

prefetcher/next_line_l2c/%.o: CFLAGS += -Iprefetcher/next_line_l2c
prefetcher/next_line_l2c/%.o: CXXFLAGS += -Iprefetcher/next_line_l2c
obj/cpu0l2cprefetcher.a: $(patsubst %.cc,%.o,$(wildcard prefetcher/next_line_l2c/*.cc)) $(patsubst %.c,%.o,$(wildcard prefetcher/next_line_l2c/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

branch/bimodal/%.o: CFLAGS += -Ibranch/bimodal
branch/bimodal/%.o: CXXFLAGS += -Ibranch/bimodal
obj/cpu0branch_predictor.a: $(patsubst %.cc,%.o,$(wildcard branch/bimodal/*.cc)) $(patsubst %.c,%.o,$(wildcard branch/bimodal/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

btb/basic_btb/%.o: CFLAGS += -Ibtb/basic_btb
btb/basic_btb/%.o: CXXFLAGS += -Ibtb/basic_btb
obj/cpu0btb.a: $(patsubst %.cc,%.o,$(wildcard btb/basic_btb/*.cc)) $(patsubst %.c,%.o,$(wildcard btb/basic_btb/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

prefetcher/next_line_llc/%.o: CFLAGS += -Iprefetcher/next_line_llc
prefetcher/next_line_llc/%.o: CXXFLAGS += -Iprefetcher/next_line_llc
obj/cpu0llprefetcher.a: $(patsubst %.cc,%.o,$(wildcard prefetcher/next_line_llc/*.cc)) $(patsubst %.c,%.o,$(wildcard prefetcher/next_line_llc/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

replacement/lru_llc/%.o: CFLAGS += -Ireplacement/lru_llc
replacement/lru_llc/%.o: CXXFLAGS += -Ireplacement/lru_llc
obj/cpu0llreplacement.a: $(patsubst %.cc,%.o,$(wildcard replacement/lru_llc/*.cc)) $(patsubst %.c,%.o,$(wildcard replacement/lru_llc/*.c))
	@mkdir -p $(dir $@)
	ar -rcs $@ $^

-include $(wildcard prefetcher/*/*.d)
-include $(wildcard branch/*/*.d)
-include $(wildcard btb/*/*.d)
-include $(wildcard replacement/*/*.d)
-include $(wildcard src/*.d)

