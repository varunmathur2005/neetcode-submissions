class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        word_buffer = []
        cur_len = 0
        for w in words:
            # If we run out of space then adjust the buffer
            # Need unit spacing between each word in the buffer
            if cur_len + len(w) + len(word_buffer) > maxWidth:
                total_spaces = maxWidth - cur_len
                gaps = len(word_buffer) - 1

                # Single word
                if gaps == 0:
                    line = word_buffer[0] + (" " * total_spaces)
                else:
                    space_div, remainder = divmod(total_spaces, gaps)
                
                    line = word_buffer[0]
                    for i in range(1, len(word_buffer)):
                        spaces = space_div
                        if remainder:
                            spaces += 1
                            remainder -= 1
                        line += (" " * spaces) + word_buffer[i]
                
                res.append(line)
                word_buffer, cur_len = [], 0

            word_buffer.append(w)
            cur_len += len(w)
        
        # Flush out the buffer (last line)
        line = " ".join(word_buffer)
        word_spaces = maxWidth - len(line)
        line += " " * word_spaces
        res.append(line)

        return res


