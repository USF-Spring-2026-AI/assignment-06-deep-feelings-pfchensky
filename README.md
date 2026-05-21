[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mW4WPbr-)
# A06 - Deep Feelings

This is an optional assignment for AI (Spring 2026). See assignment details on Canvas.

For the enhanced system, I choosed remove stopwords and bigram features.

Answer the following questions for all enhancements which did NOT lead to increased performance:<br> 
+ Why did the changes not result in the increased performance?<br>
Answer: The baseline system accuracy is 0.6572. The embeddings accuracy is: 0.5842. The embeddings did not improve performance. Embeddings convert each text into a vector, so some important sentiment words may be weakened. Sentiment analysis often depends on exact words such as “good,” “bad,” “not good,” and “very bad.” Bag of Words can preserve these features more directly than embeddings.<br>

+ How can the performance be improved?<br> 
Answer: Combining embedding with Bag of words and bigram.<br>

Answer the following questions for all enhancements which DID lead to increased performance:<br> 

+ What was the magnitude of the performance increase?<br> 
The baseline system accuracy is 0.6572.The enhanced system accuracy is 0.6626.So the performance just increased a little bit :0.6626-0.6572=0.0054

+ Other than the specific enhancements, could the performance increase be due to any other factors?<br>
I ran two additional experiments. One only removed stopwords, the accuracy was 0.6504, which was lower than the baseline. The other used only bigrams, the accuracy was 0.6614, which was a little bit higher than the baseline. Therefore, the main improvement came from using bigrams. Based on the two experiments, the accuracy increase may be related to the test data. If the test data contains many useful two-word phrases such as “not good”, “not bad”, the bigram system can capture these phrases better than the baseline system. This may help improve the accuracy.<br>
