# Тематическое моделирование метрически гомогенных корпусов наивной поэзии

### В репозитории находятся 11 файлов:
1. main.ipynb - препроцессинг текстов и тренировка модели, результаты сохраняются в csv- и txt-файл;
2. jaccard_similarity.ipynb - определение коэффициентов сходства Жаккара между размерами, результаты визуализируются тепловой картой; 
3. semantic_domains.ipynb - распределение тем по семантическим доменам, результаты визуализируются тепловой картой и графом;
4. pareto_dist.ipynb - сравнение распределения частотности размеров с распределением Парето;
5. count_tokens.ipynb - подсчет объема корпуса в токенах, результаты записываются в csv-файл;
6. sort_corpus_by_meter.ipynb - сортировка документов всего корпуса наивной поэзии на корпуса по стихотворным размерам;
7. sort_by_ending.py - сортировка документов всего корпуса на корпуса по типу клаузулы;
8. clean_endings_corp.py - фильтрация корпусов по типу клаузулы, удаление невалидных файлов;
9. 10_topics.csv - результаты работы модели на 10 топиков;
10. 10_topics_strict.csv - результаты работы модели на 10 топиков со строгими настройками min_df и max_df (основные результаты);
11. 30_topics.csv - результаты работы модели на 30 топиков. 
 
***
# Topic modeling of metrically homogeneous corpora of naïve poetry

### The repository contains 11 files:
1. main.ipynb - preprocessing and modeling of the corpora, the results are saved as a csv- and a txt-file;
2. jaccard_similarity.ipynb - determining Jaccard similarity between meters, the results are then visualized as a heatmap;
3. semantic_domains.ipynb - assigning topics to the semantic domain they are closest to, the results are then visualized as a graph and a heatmap;
4. pareto_dist.ipynb - comparing the distribution of corpora sizes and Pareto distribution;
5. count_tokens.ipynb - counting corpora sizes in tokens, the results are saved as a csv-file;
6. sort_corpus_by_meter.ipynb - sorting the documents of naive poetry corpus by meter and saving to individual files;
7. sort_by_ending.py - sorting the documents of naive poetry corpus by ending type;
8. clean_endings_corp.py - filtering the ending-type corpora and deleting invalid files;
9. 10_topics.csv - results of modeling with 10 topics;
10. 10_topics_strict.csv - results of modeling with stricter min_df and max_df parameters (main results);
11. 30_topics.csv - results of modeling with 30 topics. 
