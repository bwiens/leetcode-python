#!/usr/bin/python
# Benjamin Wiens
# Before And After Puzzle (https://leetcode.com/problems/before-and-after-puzzle/)

phrases = ["writing code","code rocks"]

class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        last, result = {}, []
        for index, phrase in enumerate(phrases):
            splitted = phrase.split()
            #last[splitted[-1]] = ' '.join(splitted[:-1])
            if splitted[-1] not in last:
                last[splitted[-1]] = index
            else:
                already = last.get(splitted[-1])
                if isinstance(already,int):
                    last[splitted[-1]] = index, already
                else:
                    current_list = []
                    for number in already:
                        current_list.append(number)
                    current_list.append(index)
                    last[splitted[-1]] = current_list
        for index, phrase in enumerate(phrases):
            splitted = phrase.split()
            if splitted[0] in last:
                #if one
                if isinstance(last.get(splitted[0]), int):
                    if index != last.get(splitted[0]):
                        process = phrases[last.get(splitted[0])]
                        process_split = process.split()
                        if len(process_split) > 1:
                            new_phrase = ' '.join(process_split[:-1]) + ' ' + ' '.join(splitted[0:])
                        else:
                            new_phrase = ' '.join(process_split[:-1]) + '' + ' '.join(splitted[0:])
                        if new_phrase not in result:
                            result.append(new_phrase)
                #if multiple
                else:
                    current_list = last.get(splitted[0])
                    for number in current_list:
                        if index != number:
                            process = phrases[number]
                            process_split = process.split()
                            if len(process_split) > 1:
                                new_phrase = ' '.join(process_split[:-1]) + ' ' + ' '.join(splitted[0:])
                            else:
                                new_phrase = ' '.join(process_split[:-1]) + '' + ' '.join(splitted[0:])
                            if new_phrase not in result:
                                result.append(new_phrase)

        result.sort()
        return result

print(Solution().beforeAndAfterPuzzles(phrases))
