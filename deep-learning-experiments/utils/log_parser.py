

class log_parser:
    block_deliminator = "-----------------------------------------------------------------"
    line_heads_metrics = [
        "loss:",
        "accuracy:",
        "consensus_distance:",
    ]
    line_heads_timer = [
        "- data loading",
        "- eval on global train",
        "- eval on test",
        "- gossip averaging",
        "- model update",
        "- update moving average",
        "- Total time",
    ]

    def __init__(self, log_file):
        self.log_file = log_file
        self.fp = open(self.log_file, "r")

        self.log_block = []

    def __del__(self):
        self.fp.close()

    def parse(self):
        for line in self.fp:
            if line.startswith(self.block_deliminator):
                yield self.parse_block()

            self.log_block.append(line)

    def parse_block(self):
        res_dict = {}
        for head in (self.line_heads_metrics + self.line_heads_timer):
            res_dict[head] = []


        for line in self.log_block:

            for head in self.line_heads_metrics:
                if line.startswith(head):
                    tag_name = "value:"
                    format_number_len = 7
                    value_idx = line.find(tag_name)
                    value = float(line[value_idx + len(tag_name) :value_idx + len(tag_name) + format_number_len ])

                    res_dict[head].append(value)
            
            # timer log
            for head in self.line_heads_timer:
                if line.startswith(head):
                    pass



