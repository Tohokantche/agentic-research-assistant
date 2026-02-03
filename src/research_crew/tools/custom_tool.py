from crewai.tools import BaseTool
from pydantic import ConfigDict
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain_community.tools.gmail.send_message import GmailSendMessage


class SendEmailTool(BaseTool):
     name: str = "Email Tool"
     description: str = (
         """
           Useful to send an email daraft.
             The input to this tool should be a pipe (|) separated text
             of length 3 (three), representing who to send the email to,
             the subject of the email and the actual message.
             For example, "lorem@ipsum.com|Nice To Meet You|Hey it was great to meet you.".
             and also send the email
         """
         )
     
     model_config = ConfigDict(arbitrary_types_allowed=True)
     def _run(self,argument:str) -> str:
         email, subject, message = argument.split("|")
         gmail = GmailToolkit()
         draft = GmailCreateDraft(api_resource=gmail.api_resource)
         draft2 = GmailSendMessage(api_resource=gmail.api_resource)
         result = draft({"to": [email], "subject": subject, "message": message})
         result2 = draft2({"to": [email], "subject": subject, "message": message})
         return f"\nDraft created: {result}\n Email Sent {result2}" 
     

class SentimentClassificationTool(BaseTool):
     name: str = "Email Tool"
     description: str = (
         """
           Useful to evalute the polarity (sentiment) of a sentence.
             The input to this tool should be a text string.
             For example, "I love Python! It's simple, powerful, and versatile.".
             The output is formated as : {'neg': 0.0, 'neu': 0.253, 'pos': 0.747, 'compound': 0.8519}.
             The compound score normalizes the sentiment into a range from -1 (most negative) to 1 (most positive)
         """
         )
     
     model_config = ConfigDict(arbitrary_types_allowed=True)
     def _run(self,argument:str) -> str:
        try:
            nltk.data.find('sentiment/vader_lexicon.zip')
        except nltk.downloader.DownloadError:
            nltk.download('vader_lexicon')
        sia = SentimentIntensityAnalyzer()
        # Get sentiment scores
        score = sia.polarity_scores(argument)
        return score
     