API reference
=============

**anomaly**: Anomaly detection
-------------------------------

The estimators in ``anomaly`` are slightly different than the rest of the estimators. Instead of a ``predict_one`` method, each anomaly detector has a ``score_one`` method which returns an anomaly score for a given set of features. Anomalies will have high scores whereas normal observations will have low scores. The range of the scores depends on the estimator. 

.. rubric:: Classes

.. currentmodule:: creme.anomaly
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    HalfSpaceTrees


**base**: Base interfaces
--------------------------

Every estimator in ``creme`` is a class, and as such inherits from at least one base interface. These are used to categorize, organize, and standardize the many estimators that ``creme`` contains. 

.. rubric:: Classes

.. currentmodule:: creme.base
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    AnomalyDetector
    BinaryClassifier
    Clusterer
    Ensemble
    Estimator
    MultiClassifier
    MultiOutputClassifier
    MultiOutputRegressor
    Regressor
    Transformer
    Wrapper


**cluster**: Unsupervised clustering
-------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.cluster
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    KMeans


**compat**: Compatibility with other libraries
-----------------------------------------------

This module contains adapters for making ``creme`` estimators compatible with other libraries, and vice-versa whenever possible. 

.. rubric:: Classes

.. currentmodule:: creme.compat
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Creme2SKLClassifier
    Creme2SKLClusterer
    Creme2SKLRegressor
    Creme2SKLTransformer
    PyTorch2CremeRegressor
    SKL2CremeClassifier
    SKL2CremeRegressor

.. rubric:: Functions

.. currentmodule:: creme.compat
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: function.rst
        
    convert_creme_to_sklearn
    convert_sklearn_to_creme


**compose**: Models composition
--------------------------------

.. rubric:: Classes

.. currentmodule:: creme.compose
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Blacklister
    FuncTransformer
    Pipeline
    Renamer
    TransformerUnion
    Whitelister


**datasets**: Datasets
-----------------------

.. rubric:: Classes

.. currentmodule:: creme.datasets
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Airline
    ChickWeights
    CreditCard
    Elec2
    KDD99HTTP
    MaliciousURL
    Phishing
    Restaurants
    SMSSpam
    TREC07
    ToulouseBikes
    TrumpApproval


**decomposition**: Online matrix decomposition
-----------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.decomposition
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    LDA


**dummy**: Dummy estimators
----------------------------

.. rubric:: Classes

.. currentmodule:: creme.dummy
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    NoChangeClassifier
    PriorClassifier
    StatisticRegressor


**ensemble**: Ensemble learning
--------------------------------

.. rubric:: Classes

.. currentmodule:: creme.ensemble
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    AdaBoostClassifier
    BaggingClassifier
    BaggingRegressor
    HedgeRegressor
    StackingBinaryClassifier


**feature_extraction**: Feature extraction from a stream
---------------------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.feature_extraction
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Agg
    BoW
    Differ
    TFIDF
    TargetAgg


**feature_selection**: Online feature selection
------------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.feature_selection
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    RandomDiscarder
    SelectKBest
    VarianceThreshold


**imblearn**: Imbalanced learning
----------------------------------

.. rubric:: Classes

.. currentmodule:: creme.imblearn
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    RandomOverSampler
    RandomSampler
    RandomUnderSampler


**impute**: Missing data imputation
------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.impute
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    PreviousImputer
    StatImputer


**linear_model**: Linear models
--------------------------------

.. rubric:: Classes

.. currentmodule:: creme.linear_model
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    FMRegressor
    LinearRegression
    LogisticRegression
    PAClassifier
    PARegressor
    PoissonRegression
    SoftmaxRegression


**meta**: Meta-models that work by wrapping other models
---------------------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.meta
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    BoxCoxRegressor
    TransformedTargetRegressor


**metrics**: Streaming metrics
-------------------------------

.. rubric:: Classes

.. currentmodule:: creme.metrics
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Accuracy
    ClassificationReport
    ConfusionMatrix
    CrossEntropy
    F1
    FBeta
    Jaccard
    LogLoss
    MAE
    MCC
    MSE
    MacroF1
    MacroFBeta
    MacroPrecision
    MacroRecall
    MicroF1
    MicroFBeta
    MicroPrecision
    MicroRecall
    MultiFBeta
    Precision
    RMSE
    RMSLE
    ROCAUC
    Recall
    RegressionMultiOutput
    Rolling
    SMAPE
    WeightedF1
    WeightedFBeta
    WeightedPrecision
    WeightedRecall


**model_selection**: Model selection and evaluation
----------------------------------------------------

.. rubric:: Functions

.. currentmodule:: creme.model_selection
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: function.rst
        
    expand_param_grid
    progressive_val_score
    successive_halving


**multiclass**: Multi-class classification
-------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.multiclass
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    OneVsRestClassifier


**multioutput**: Multi-output classification and regression
------------------------------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.multioutput
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    ClassifierChain
    RegressorChain


**naive_bayes**: Naive Bayes algorithms
----------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.naive_bayes
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    BernoulliNB
    ComplementNB
    GaussianNB
    MultinomialNB


**neighbors**: Neighbors-based learning
----------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.neighbors
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    KNeighborsClassifier
    KNeighborsRegressor


**optim**: Online optimization
-------------------------------

.. rubric:: Classes

.. currentmodule:: creme.optim
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    AMSGrad
    AdaBound
    AdaDelta
    AdaGrad
    AdaMax
    Adam
    FTRLProximal
    MiniBatcher
    Momentum
    NesterovMomentum
    Optimizer
    RMSProp
    SGD

Weight initialization schemes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    initializers.Constant
    initializers.Normal
    initializers.Zeros

Loss functions
~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    losses.Absolute
    losses.Cauchy
    losses.CrossEntropy
    losses.EpsilonInsensitiveHinge
    losses.Hinge
    losses.Log
    losses.Poisson
    losses.Quantile
    losses.Squared

Learning rate schedulers
~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    schedulers.Constant
    schedulers.InverseScaling
    schedulers.Optimal


**preprocessing**: Feature preprocessing
-----------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.preprocessing
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    FeatureHasher
    MinMaxScaler
    Normalizer
    OneHotEncoder
    PolynomialExtender
    StandardScaler


**proba**: Probability distributions
-------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.proba
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Gaussian
    Multinomial


**reco**: Recommender systems
------------------------------

.. rubric:: Classes

.. currentmodule:: creme.reco
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    RandomNormal
    SGDBaseline
    SVD


**stats**: Running statistics
------------------------------

.. rubric:: Classes

.. currentmodule:: creme.stats
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    AutoCorrelation
    BayesianMean
    Bivariate
    Count
    Covariance
    EWMean
    EWVar
    Entropy
    IQR
    Kurtosis
    Max
    Mean
    Min
    Mode
    NUnique
    PeakToPeak
    PearsonCorrelation
    Quantile
    RollingIQR
    RollingMax
    RollingMean
    RollingMin
    RollingMode
    RollingPeakToPeak
    RollingQuantile
    RollingSEM
    RollingSum
    RollingVar
    SEM
    Skew
    Sum
    Univariate
    Var


**stream**: Helper functions for streaming data
------------------------------------------------

.. rubric:: Functions

.. currentmodule:: creme.stream
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: function.rst
        
    iter_array
    iter_csv
    iter_pandas
    iter_sklearn_dataset
    iter_vaex
    shuffle


**time_series**: Time series forecasting
-----------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.time_series
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Detrender
    GroupDetrender
    SNARIMAX


**tree**: Decision trees
-------------------------

.. rubric:: Classes

.. currentmodule:: creme.tree
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    DecisionTreeClassifier
    RandomForestClassifier


**utils**: Utility classes and functions
-----------------------------------------

.. rubric:: Classes

.. currentmodule:: creme.utils
.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        
    Histogram
    SDFT
    Skyline
    SortedWindow
    Window

Utilities for unit testing and sanity checking estimators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        

Mathematical utility functions mostly intended for internal purposes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        

Helper functions for making things readable by humans
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    :toctree: generated/
    :nosignatures:
    :template: class.rst
        


