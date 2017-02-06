class ParsedObject:
    
    name = ''
    extension = ''
    singleComment = ''
    blockFront = ''
    blockBack = ''

    def __init__(self, nameInput, extensionInput, singleCommentInput, blockCommentFrontInput, blockCommentBackInput):
        ParsedObject.name = nameInput
        ParsedObject.extension = extensionInput
        ParsedObject.singleComment = singleCommentInput
        self.setBlockComment(blockCommentFrontInput, blockCommentBackInput)

    @staticmethod
    def setBlockComment(front, back):
        ParsedObject.blockFront = front
        ParsedObject.blockBack = back
