#!/usr/bin/env python3
import argparse
import json


# Parse through comnand arguments and do stuff
def read_command_args():
    parser = argparse.ArgumentParser(
        description='Test for anagram awesomeness')
    parser.add_argument('words', type=str, nargs=2, action='store',
                        help='Provide 2 words to test for anagram-ness. Any additional words will be ignored!')
    parser.add_argument('--version', '-v', action='version',
                        version='%(prog)s 0.1')
    args, unknown = parser.parse_known_args()

    if anagram_check(args.words[0], args.words[1]):
        print('True')
    else:
        print('False')


# Check 2 words as anagrams, return true/false
def anagram_check(first, second):
    if(sorted(first) == sorted(second)):
        return True
    else:
        return False


# AWS Lambda Compat
def lambda_handler(event, context):
    if anagram_check(event['word0'], event['word1']):
        return {
            'statusCode': 200,
            'body': json.dumps('True')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('False')
        }


# Starts the party [if CLI]
if __name__ == '__main__':
    read_command_args()
