# Metal Scream Classifier

Fans of heavy metal often have very particular tastes when it comes to their favourite music. Subtle differences in tempo, aggression, tone, and especially vocals can be key deciding factors in a metalhead's preferences. Fans of death metal or doom metal might prefer deathly, low-pitched growls, thrash metal and black metal fans might prefer high-pitched, agonized fry screams, and traditional heavy metal enjoyers might only like soaring clean vocals. Therefore, the problem of classifying songs by their scream type could be beneficial for organizers and streaming services in order to make meaningful event and music reccommendations to fans.

This project will attempt to use a variety of machine learning methods to classify audio snippets of heavy metal screams into five categories:
- `lowfry`
- `midfry`
- `highfry`
- `layered` (Multiple vocals at once)
- `clean`

## Dataset

We will use the [**`scream_detection_heavy_metal`**](https://huggingface.co/datasets/jpdiazpardo/scream_detection_heavy_metal) dataset openly available on [Hugging Face](https://huggingface.co/), curated by Vedant Kalbag and Alexander Lerch from the Music Informatics Group at the Georgia Institute of Technology, USA. 

## Context

Previous work by the curators of the dataset has been done on this problem, with limited performance due to significant class imbalance. Their results can be accessed [here](https://arxiv.org/pdf/2205.05580). This project will attempt to expand on these results by experimenting with similar feature transformations, as well as other classical models, audio transformers, deep learning models, and pretrained models. 

## References

1. Kalbag, Vedant, and Alexander Lerch. ArXiv, vol. 2205.05580, 2022.

