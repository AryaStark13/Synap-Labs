# Langchain Model Training Wizard (MTW) PRD

## 1. What Are We Solving For?
We are introducing a Model Training Wizard (MTW) to help users create their own custom language models. The problem we are solving is that users may have specific needs that are not met by our suite of pretrained LLMs. This feature is for users who want to create high-quality models tailored to their specific needs.

## 2. Why Does It Matter?
This initiative matters because it allows users to create models that are tailored to their specific needs. This can lead to better performance and accuracy in their language processing tasks. We have conducted customer research that shows a strong demand for this feature.

## 3. What Does Success Look Like?
The primary metric we will use to gauge success is the number of custom models created using the MTW. Our target is to have 100 custom models created within the first 6 months of launch. The secondary metric of success is user satisfaction with the MTW, as measured by a survey sent to users after they have created a custom model.

## 4. Background
Our research has shown that many users have specific language processing needs that are not met by our suite of pretrained LLMs. This has led to a demand for a feature that allows users to create their own custom models. Competitors in the market have already introduced similar features, and we believe that this is a necessary addition to our product.

## 5. Known Constraints
The MTW must be user-friendly and accessible to users with varying levels of technical expertise. It must also be able to handle large datasets and provide performance evaluation metrics in a timely manner. We must also ensure that the MTW complies with all legal and business guardrails.

## 6. Solution Proposal
We propose introducing a Model Training Wizard (MTW) that provides step-by-step instructions, dataset management tools, and performance evaluation metrics to help users create high-quality models tailored to their specific needs. The MTW will be accessible from the Langchain dashboard and will guide users through the process of creating a custom model.

## 7. Risks & Assumptions
We assume that users will be able to provide high-quality datasets for training their custom models. We also assume that the MTW will be user-friendly and accessible to users with varying levels of technical expertise. The main risk is that users may not be satisfied with the performance of their custom models, which could lead to negative feedback and a decrease in user engagement.

## 8. Target Customers
### 8.1 Market
The MTW will be available to all users of Langchain, regardless of their location or industry.
### 8.2 Audience Segments
The MTW is targeted towards users who have specific language processing needs that are not met by our suite of pretrained LLMs. This includes researchers, developers, and businesses that require highly specialized language models.

## 9. User Experience
### 9.1 User Flows
The user flow for the MTW will be as follows:
1. User selects "Create Custom Model" from the Langchain dashboard
2. User is guided through the process of uploading their dataset and selecting training parameters
3. User is provided with performance evaluation metrics and the option to fine-tune their model
4. User can save their custom model and use it in their language processing tasks

## 10. High Level Use Cases

|    	| Name                                                       	| Description                                                                                                                                            	| PDT or Squad                                                                           	| Dependency?                                                                 	| Priority                                    	| Open Questions,  Notes & Discussions                                             	|
|----	|------------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------	|---------------------------------------------	|----------------------------------------------------------------------------------	|
| 1 	| Upload Dataset                                             	| User uploads their dataset to the MTW                                                                                                                 	| Data Science Team                                                                       	| None                                                                        	| MUST HAVE                                    	|                                                                                  	|
| 2 	| Select Training Parameters                                  	| User selects the training parameters for their custom model                                                                                            	| Data Science Team                                                                       	| None                                                                        	| MUST HAVE                                    	|                                                                                  	|
| 3 	| Performance Evaluation                                      	| User is provided with performance evaluation metrics for their custom model and the option to fine-tune it                                            	| Data Science Team                                                                       	| None                                                                        	| MUST HAVE                                    	|                                                                                  	|
| 4 	| Save Custom Model                                           	| User can save their custom model and use it in their language processing tasks                                                                         	| Data Science Team                                                                       	| None                                                                        	| MUST HAVE                                    	|                                                                                  	|

## 11. Rollout Approach
We will execute a gradual scale-up rollout of the MTW, starting with a small group of beta testers and gradually expanding to all users. We will use A/B testing to measure the impact of the MTW on user engagement and satisfaction. We will work closely with our partners in Analytics, Data Science, and Business Operations to ensure that the rollout is successful.

## 12. Measuring Success
We will measure the success of the MTW by tracking the number of custom models created using the feature and user satisfaction with the MTW, as measured by a survey sent to users after they have created a custom model. We will provide regular performance readouts to ensure that we are meeting our targets.