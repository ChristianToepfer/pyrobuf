import unittest

class MessageComments(unittest.TestCase):
     def test_message_block_comment_line(self):
        from test_message_comments_proto import TestBlockMessageCommentLine
        self.assertEqual(TestBlockMessageCommentLine.__doc__, '\n    Message with block comment in one line\n    ')
     def test_message_block_comment(self):
        from test_message_comments_proto import TestBlockMessageComment
        self.assertEqual(TestBlockMessageComment.__doc__, '\n    Message with block comment\n    ')
     def test_message_line_comment(self):
        from test_message_comments_proto import TestLineMessageComment
        self.assertEqual(TestLineMessageComment.__doc__, '\n    Message with line comment\n    ')
     def test_message_block_comment_multi(self):
        from test_message_comments_proto import TestBlockMessageComments
        self.assertEqual(TestBlockMessageComments.__doc__, '\n    Message with multiline block comment\n\nMore details\n"stop"\n    ')
     def test_field_message_comment_standard(self):
        from test_message_comments_proto import TestFieldMessageCommentStandard
        self.assertEqual(TestFieldMessageCommentStandard.hello.__doc__, 'Hello comment ')
     def test_field_message_comment_before(self):
        from test_message_comments_proto import TestFieldMessageCommentBefore
        self.assertEqual(TestFieldMessageCommentBefore.hello.__doc__, 'Hello comment before definition ')
     def test_field_message_comment_long(self):
        from test_message_comments_proto import TestFieldMessageCommentLong
        self.assertEqual(TestFieldMessageCommentLong.hello.__doc__, 'Hello long block comment\nwith several lines ')
