# vk-hse-news-tags
### Навигация
**Gradio: https://d61f438b1b08d1d4c5.gradio.live/**
1. В data-preparation.ipynb и concating.ipynb подготовка датасета
2. В word2vec.ipynb бейзлайн Word2Vec + CatBoost, weighted F1 = 0.73
3. В tfidf_baseline.ipynb бейзлайн с tfidf + CatBoost + PCA, weighted F1 = 0.81
4. В classifier-training-ipynb обучение rubert-tiny2 + головы-классификатора (эта версия не использовалась), но были получены метрики ROC AUC (ovo, ovr) ~ 0.989, F1 Weighted ~ 0.827
5. neural_classifier_final.ipynb - блокнот с тренировкой одного из трех классификаторов, которые далее были объединены в ансамбль с подобранными коэффицикетами. F1 Weighted всего ансамбля ~ 0.91, ROC AUC (ovo, ovr) ~ 0.995 -> п. 6
6. В ensemble.ipynb подбор весов в ансамбле моделей, максимизирующих целевые метрики
7. В heads-training.ipynb тренировка классификаторов на основе bert моделей. Все 3 головы имеют разные берт модели и одинаковые классификаторы, из-за чего их обучение идентично.


```
{           "selected_label": "категория из списка",
            "prob": 0.8,
            "hashtags": ["хэштэг1", "хэштэг2", ...], 
            "keywords": ["ключевое слово1", "ключевое слово2", ...]
}
```
