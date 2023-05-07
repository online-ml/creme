# Regression



=== "Table"

    | Model                                    | Dataset       |        MAE |      RMSE |            R2 |   Memory in Mb |   Time in s |
    |:-----------------------------------------|:--------------|-----------:|----------:|--------------:|---------------:|------------:|
    | Adaptive Model Rules                     | ChickWeights  |  24.0925   |  37.1369  |    0.719675   |    0.0469542   |    5.03028  |
    | Adaptive Model Rules                     | TrumpApproval |   1.40204  |   2.43644 |   -1.02749    |    0.114429    |    5.76779  |
    | Adaptive Random Forest                   | ChickWeights  |  25.9648   |  40.6034  |    0.6649     |    1.18613     |   32.8286   |
    | Adaptive Random Forest                   | TrumpApproval |   0.801133 |   2.11603 |   -0.529292   |    1.28362     |   54.6942   |
    | Bagging                                  | ChickWeights  |  23.0595   |  36.5862  |    0.727928   |    0.643575    |   19.8658   |
    | Bagging                                  | TrumpApproval |   0.904415 |   2.23483 |   -0.705833   |    1.33501     |   42.6904   |
    | Exponentially Weighted Average           | ChickWeights  | 120.54     | 139.462   |   -2.95334    |    0.183387    |   12.3806   |
    | Exponentially Weighted Average           | TrumpApproval |  40.7536   |  40.7895  | -567.257      |    0.316642    |   30.0432   |
    | Hoeffding Adaptive Tree                  | ChickWeights  |  23.2557   |  37.579   |    0.712962   |    0.0946112   |    5.75782  |
    | Hoeffding Adaptive Tree                  | TrumpApproval |   0.910675 |   2.2343  |   -0.705019   |    0.138225    |    6.69917  |
    | Hoeffding Tree                           | ChickWeights  |  23.0842   |  36.6638  |    0.726773   |    0.0440512   |    4.02236  |
    | Hoeffding Tree                           | TrumpApproval |   0.949745 |   2.24815 |   -0.726224   |    0.148639    |    9.13796  |
    | Linear Regression                        | ChickWeights  |  23.8353   |  37.0287  |    0.721307   |    0.00421047  |    2.10647  |
    | Linear Regression                        | TrumpApproval |   1.3486   |   4.12828 |   -4.82084    |    0.00497341  |    3.6327   |
    | Linear Regression with l1 regularization | ChickWeights  |  23.868    |  37.0773  |    0.720575   |    0.00444126  |    1.13401  |
    | Linear Regression with l1 regularization | TrumpApproval |   1.21585  |   4.06821 |   -4.65269    |    0.0052042   |    2.06156  |
    | Linear Regression with l2 regularization | ChickWeights  |  25.5204   |  38.6553  |    0.696284   |    0.00423336  |    1.11618  |
    | Linear Regression with l2 regularization | TrumpApproval |   1.99918  |   4.40997 |   -5.64232    |    0.0049963   |    1.98704  |
    | Passive-Aggressive Regressor, mode 1     | ChickWeights  |  24.2339   |  37.5576  |    0.713289   |    0.00345898  |    1.33977  |
    | Passive-Aggressive Regressor, mode 1     | TrumpApproval |   4.90639  |   6.6656  |  -14.1749     |    0.00443554  |    2.18425  |
    | Passive-Aggressive Regressor, mode 2     | ChickWeights  |  99.5681   | 141.4     |   -3.06396    |    0.00345898  |    1.99155  |
    | Passive-Aggressive Regressor, mode 2     | TrumpApproval |  31.1288   |  34.4257  | -403.774      |    0.00443554  |    2.19594  |
    | River MLP                                | ChickWeights  |  49.5783   |  77.9026  |   -0.233541   |    0.0123129   |   18.4913   |
    | River MLP                                | TrumpApproval |   1.59139  |   5.147   |   -8.04808    |    0.0133505   |   30.7873   |
    | Stochastic Gradient Tree                 | ChickWeights  |  68.1198   |  79.5649  |   -0.286746   |    1.12059     |    9.48214  |
    | Stochastic Gradient Tree                 | TrumpApproval |   9.43874  |  17.9468  | -109.008      |    3.08244     |   24.6638   |
    | Streaming Random Patches                 | ChickWeights  |  23.5162   |  38.2072  |    0.703285   |    0.558536    |   50.7829   |
    | Streaming Random Patches                 | TrumpApproval |   0.640561 |   1.97134 |   -0.32731    |    1.05934     |  101.873    |
    | [baseline] Mean predictor                | ChickWeights  |  49.4914   |  70.2457  |   -0.00297194 |    0.000490189 |    0.529127 |
    | [baseline] Mean predictor                | TrumpApproval |   1.56814  |   2.20374 |   -0.658701   |    0.000490189 |    0.8379   |
    | k-Nearest Neighbors                      | ChickWeights  |  22.9043   |  34.7945  |    0.753924   |    0.0461216   |    4.35991  |
    | k-Nearest Neighbors                      | TrumpApproval |   0.493975 |   1.50807 |    0.223232   |    0.0660038   |    9.48546  |

=== "Chart"

    *Try reloading the page if something is buggy*

    ```vegalite
    {
      "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
      "data": {
        "values": [
          {
            "step": 11,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 32.364564569910335,
            "RMSE": 32.97872020361878,
            "R2": -1398.9905780691188,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.003051
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 22.977933628105813,
            "RMSE": 25.38362603225939,
            "R2": -681.3960169454474,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.0083
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 16.216942910977988,
            "RMSE": 20.82463881551788,
            "R2": -300.18738429635704,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.014943
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 12.450847696587651,
            "RMSE": 18.04722398474583,
            "R2": -255.42929659358052,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.023007
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 11.8883407017882,
            "RMSE": 18.699705575978975,
            "R2": -67.26141846932143,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.032524
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 11.481406471145082,
            "RMSE": 17.562600262725994,
            "R2": -24.95549321582236,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.043462
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 10.781108661026623,
            "RMSE": 16.493572764286025,
            "R2": -14.34295652053857,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.055844
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 9.717703273355898,
            "RMSE": 15.46585610846664,
            "R2": -11.231382330967593,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.069657
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 8.826979124235404,
            "RMSE": 14.601347274688614,
            "R2": -8.118374730562003,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.084902
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 8.34720326953035,
            "RMSE": 13.931298318002057,
            "R2": -4.796525071049026,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.101965
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 8.037877082888846,
            "RMSE": 13.41080638289134,
            "R2": -3.136902586442697,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.120474
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.656433924417384,
            "RMSE": 12.898278689410905,
            "R2": -2.1275837609073576,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.140407
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.307942088554156,
            "RMSE": 12.437137940834392,
            "R2": -1.3553409371460328,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.161783
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.037714222368383,
            "RMSE": 12.042115748312936,
            "R2": -0.8765797740197239,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.184594
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.129031762481882,
            "RMSE": 11.913307711374014,
            "R2": -0.4764258010150459,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.208855
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.184514897799321,
            "RMSE": 11.77636646389892,
            "R2": -0.1632359842489146,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.23453
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.115123062484693,
            "RMSE": 11.572523949602724,
            "R2": 0.0802677819230903,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.261536
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.006474290899419,
            "RMSE": 11.366304822809298,
            "R2": 0.2942397460202306,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.289991
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.129008217053805,
            "RMSE": 11.440940870898142,
            "R2": 0.4105268603250641,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.319876
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.62421928608864,
            "RMSE": 12.045617517752785,
            "R2": 0.4279229250366536,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.351191
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.729844807682863,
            "RMSE": 12.068921171072352,
            "R2": 0.5087708730950672,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.383941
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.873703200353374,
            "RMSE": 12.23342730557754,
            "R2": 0.5938836560989084,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.4181169999999999
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 7.894340397324045,
            "RMSE": 12.218207932001455,
            "R2": 0.6481596201604607,
            "Memory in Mb": 0.0041303634643554,
            "Time in s": 0.4537249999999999
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 8.479294890454037,
            "RMSE": 13.126132095776898,
            "R2": 0.6289858847198173,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.4907699999999999
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 8.914096443559163,
            "RMSE": 13.971715828104037,
            "R2": 0.6301108693673194,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.529253
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 9.123963222012373,
            "RMSE": 14.305597328390173,
            "R2": 0.6641373552910966,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.569186
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 9.083791720841957,
            "RMSE": 14.24670706195338,
            "R2": 0.7111028643570333,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.610599
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 9.589205789771716,
            "RMSE": 14.956254664628933,
            "R2": 0.716435491318643,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.653398
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 10.6480954226875,
            "RMSE": 17.335456678654833,
            "R2": 0.654294294845865,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.697581
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 11.061417554605155,
            "RMSE": 17.89416376383148,
            "R2": 0.6847745473646168,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.743241
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 11.240970714084437,
            "RMSE": 17.96809449059472,
            "R2": 0.7153933828209167,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.7902760000000001
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 11.393007763406809,
            "RMSE": 18.07679096199219,
            "R2": 0.7381404893604309,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.8386990000000001
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 12.251680566634816,
            "RMSE": 19.3891577397662,
            "R2": 0.7074601934283691,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.8885620000000001
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 12.75183556333798,
            "RMSE": 20.473547618215623,
            "R2": 0.7001526953506461,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.93984
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 13.120977867369843,
            "RMSE": 21.06680160073653,
            "R2": 0.7191139726408686,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 0.992561
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 13.243904830041805,
            "RMSE": 21.04850718241465,
            "R2": 0.7385587649833809,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.046701
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 14.114140715648691,
            "RMSE": 22.50284796635845,
            "R2": 0.7222415724766076,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.102244
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 14.877176135328032,
            "RMSE": 23.91912678123439,
            "R2": 0.7054123344015044,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.159239
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 15.420211528669606,
            "RMSE": 24.826921056607983,
            "R2": 0.71797392321154,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.2176479999999998
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 15.588380621816588,
            "RMSE": 24.89946727120753,
            "R2": 0.7364018543257719,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.277456
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 16.102138383202178,
            "RMSE": 25.5012042182244,
            "R2": 0.73526123694725,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.338723
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 17.19666374070754,
            "RMSE": 27.602141070792264,
            "R2": 0.7086782414730581,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.4014049999999998
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 17.97145397683086,
            "RMSE": 28.90516312323801,
            "R2": 0.7179019616037816,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.4654839999999998
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 18.29792978215437,
            "RMSE": 29.184271659667463,
            "R2": 0.728186505594778,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.531041
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 18.74962346435519,
            "RMSE": 29.70957841185893,
            "R2": 0.7350194821983969,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.597992
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 19.63242676502778,
            "RMSE": 31.145843529930996,
            "R2": 0.717244444772776,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.666343
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 20.352340621675207,
            "RMSE": 32.13418072986834,
            "R2": 0.7159654376794024,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.736162
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 21.13777985928475,
            "RMSE": 33.324214910779105,
            "R2": 0.7253645356808669,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.807369
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 21.30552841968683,
            "RMSE": 33.32197733500869,
            "R2": 0.7367405849979859,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.880014
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 22.28842093535661,
            "RMSE": 34.93191609140748,
            "R2": 0.7196038878445231,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 1.954091
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 22.98790385213596,
            "RMSE": 35.84862508987654,
            "R2": 0.7176082524890277,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 2.029559
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "ChickWeights",
            "MAE": 23.835304128485923,
            "RMSE": 37.028707868367256,
            "R2": 0.7213067136137974,
            "Memory in Mb": 0.0042104721069335,
            "Time in s": 2.106474
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 23.20376765378399,
            "RMSE": 26.086393589237737,
            "R2": -1595.1823041445402,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.006002
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 14.037845165976735,
            "RMSE": 19.010285970857197,
            "R2": -144.292318589198,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.015135
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 11.507970876430278,
            "RMSE": 16.25440462414082,
            "R2": -142.20309184289852,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.026737
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 9.557907896578074,
            "RMSE": 14.248619966820993,
            "R2": -109.38231735939875,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.04106
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 8.00119890237694,
            "RMSE": 12.784639272000032,
            "R2": -54.757167221204185,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.058228
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 6.9642139928158,
            "RMSE": 11.706689332840265,
            "R2": -38.660847151370525,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.078171
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 6.158017211594616,
            "RMSE": 10.855926078196225,
            "R2": -34.244125473921144,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.100823
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 5.477712824897756,
            "RMSE": 10.159717829752896,
            "R2": -26.22221848793916,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.126265
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 5.024407839120485,
            "RMSE": 9.597258286357787,
            "R2": -20.33422740878964,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.154466
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 4.585662202332267,
            "RMSE": 9.108145701438088,
            "R2": -18.272229834363905,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.185533
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 4.26060909213789,
            "RMSE": 8.692057179629266,
            "R2": -17.933082537971817,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.219335
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.9717866152166015,
            "RMSE": 8.326248244302885,
            "R2": -16.503720237291063,
            "Memory in Mb": 0.0048131942749023,
            "Time in s": 0.255864
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.713770572650404,
            "RMSE": 8.00217875002923,
            "R2": -15.385557669694744,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.2951479999999999
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.519033617242816,
            "RMSE": 7.718418241237259,
            "R2": -14.960370233444367,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.3371889999999999
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.3459125962612686,
            "RMSE": 7.4642342223287805,
            "R2": -13.679347912302555,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.382005
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.2142611116185447,
            "RMSE": 7.238080925352425,
            "R2": -13.486769876410833,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.429554
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 3.0579195410777067,
            "RMSE": 7.023783188903098,
            "R2": -13.41588572736102,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.479826
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.945682332324278,
            "RMSE": 6.834004497968132,
            "R2": -12.75946181118139,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.532818
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.834623050495076,
            "RMSE": 6.655478314361804,
            "R2": -12.501407484394289,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.588545
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.750580257859316,
            "RMSE": 6.492898516140861,
            "R2": -12.2130072039923,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.647075
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.6430441633874877,
            "RMSE": 6.337629923196658,
            "R2": -12.005235448499764,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.708317
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.55209658354648,
            "RMSE": 6.194505226365406,
            "R2": -11.19965041203295,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.7723099999999999
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.456089002686458,
            "RMSE": 6.059000096335146,
            "R2": -10.068304379054997,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.8388639999999999
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.366054305985814,
            "RMSE": 5.93188196569365,
            "R2": -9.364683952709628,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.907942
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.2878529832492878,
            "RMSE": 5.812913918334153,
            "R2": -8.7442989221461,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 0.979676
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.2263077878678064,
            "RMSE": 5.701877933590318,
            "R2": -8.391958889485423,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.054282
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.159275760054389,
            "RMSE": 5.596308740310266,
            "R2": -8.01424271274666,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.13157
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.121286703179314,
            "RMSE": 5.500929056902255,
            "R2": -7.917124287747498,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.211538
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.058130800812745,
            "RMSE": 5.4056516105350205,
            "R2": -7.823875188349783,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.294212
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 2.010772210317983,
            "RMSE": 5.316298216027806,
            "R2": -7.440165070210115,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.379521
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.9712240547218984,
            "RMSE": 5.232121316388296,
            "R2": -7.05039272692726,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.467481
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.918906116628168,
            "RMSE": 5.150155111235484,
            "R2": -6.654334565315682,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.558
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.87787066207154,
            "RMSE": 5.072802363597129,
            "R2": -6.372735616761029,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.651027
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.8268195769848845,
            "RMSE": 4.997758130035794,
            "R2": -6.2693000939147145,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.746732
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.786028440025988,
            "RMSE": 4.9266674679383895,
            "R2": -6.249499636750513,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.84509
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.7407901109286728,
            "RMSE": 4.857855812572241,
            "R2": -6.20325679847918,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 1.946268
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.6980813320245582,
            "RMSE": 4.791872643159282,
            "R2": -6.00468916158508,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.050093
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.6641755726043943,
            "RMSE": 4.729168490426344,
            "R2": -5.896482494172518,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.156434
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.6304504193200038,
            "RMSE": 4.6685949390255965,
            "R2": -5.751055148180852,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.265329
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.6024144632936517,
            "RMSE": 4.610765602340218,
            "R2": -5.644394777378336,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.376883
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.5772046524793362,
            "RMSE": 4.555342563217192,
            "R2": -5.556843815680599,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.490967
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.5504230286371177,
            "RMSE": 4.501494961913348,
            "R2": -5.462190804899245,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.607626
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.5213504760602443,
            "RMSE": 4.449264316210896,
            "R2": -5.302224210455831,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.72689
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.4920620594434295,
            "RMSE": 4.398585386750051,
            "R2": -5.128866413959423,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.848697
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.4631535468073946,
            "RMSE": 4.3495699730724,
            "R2": -5.018290064232882,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 2.973079
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.4376774845864433,
            "RMSE": 4.302379067062498,
            "R2": -4.985157602999735,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 3.100144
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.415413283450155,
            "RMSE": 4.2569033587476754,
            "R2": -4.909007968017405,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 3.229628
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.3929189597034646,
            "RMSE": 4.212790914002432,
            "R2": -4.847686152244137,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 3.361574
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.3689716642677323,
            "RMSE": 4.1697584324400925,
            "R2": -4.840094251784054,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 3.49595
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Linear Regression",
            "dataset": "TrumpApproval",
            "MAE": 1.348598310616665,
            "RMSE": 4.128277744647548,
            "R2": -4.8208398605179,
            "Memory in Mb": 0.0049734115600585,
            "Time in s": 3.6327
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 32.42675747760146,
            "RMSE": 33.032143455333795,
            "R2": -1403.530028209614,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.002172
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.11671120534681,
            "RMSE": 25.467535638550565,
            "R2": -685.9150105173057,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.005938
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 16.40645850052153,
            "RMSE": 20.90890407573329,
            "R2": -302.6297778360383,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.010657
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.633013937743208,
            "RMSE": 18.123648450153382,
            "R2": -257.60569409037487,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.016312
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.09340740686418,
            "RMSE": 18.75532087846616,
            "R2": -67.66805855020911,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.022822
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.723217014070244,
            "RMSE": 17.64468538999345,
            "R2": -25.19868487320792,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.030046
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.995180265837302,
            "RMSE": 16.56912334002292,
            "R2": -14.483838555564008,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.037972
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.883907021821408,
            "RMSE": 15.530287677810511,
            "R2": -11.333507781967656,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.046598
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 8.972176235897166,
            "RMSE": 14.66146594146288,
            "R2": -8.193616152032533,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.055927
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 8.50780758363674,
            "RMSE": 13.99831063395296,
            "R2": -4.852424068253989,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.066187
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 8.189643323772653,
            "RMSE": 13.479618530659062,
            "R2": -3.1794651999709123,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.077165
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.801679323915957,
            "RMSE": 12.961634417305982,
            "R2": -2.158384304610562,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.088845
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.451861020480359,
            "RMSE": 12.498785048420814,
            "R2": -1.3787482214976663,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.101232
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.149646459280303,
            "RMSE": 12.093459492377487,
            "R2": -0.8926161646086501,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.114319
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.229782522017506,
            "RMSE": 11.96532542528415,
            "R2": -0.4893471433346175,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.128105
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.272512426798904,
            "RMSE": 11.818048782353436,
            "R2": -0.1714850789711801,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.1426069999999999
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.196746625780547,
            "RMSE": 11.610365671998538,
            "R2": 0.0742429673312855,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.1578139999999999
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.1064479168500405,
            "RMSE": 11.42347112116664,
            "R2": 0.2871227171728154,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.173728
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.187961051781539,
            "RMSE": 11.470757896418933,
            "R2": 0.4074503232991815,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.1903399999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.669011107337858,
            "RMSE": 12.056664202246258,
            "R2": 0.426873173509426,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.2076519999999999
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.786810512364482,
            "RMSE": 12.097059810994589,
            "R2": 0.5064776054701067,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.2256619999999999
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.967587416991401,
            "RMSE": 12.312376354870244,
            "R2": 0.5886249568088757,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.2443719999999999
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 7.942191618805254,
            "RMSE": 12.251768500136135,
            "R2": 0.6462241186586895,
            "Memory in Mb": 0.0043611526489257,
            "Time in s": 0.2637739999999999
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 8.532657015260138,
            "RMSE": 13.159069559279288,
            "R2": 0.6271215737447722,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.2838889999999999
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 8.974527826218258,
            "RMSE": 14.016709692996267,
            "R2": 0.6277246858047626,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.3047049999999999
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.187875132430849,
            "RMSE": 14.367497338174372,
            "R2": 0.6612245262436964,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.3262349999999999
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.146460078204475,
            "RMSE": 14.316362398212211,
            "R2": 0.7082709930315267,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.3484709999999999
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.641370323857412,
            "RMSE": 15.001693346690402,
            "R2": 0.7147098761119641,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.3714179999999999
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.700825117113602,
            "RMSE": 17.38383679543193,
            "R2": 0.6523619983610591,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.3950729999999999
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.121905143066762,
            "RMSE": 17.96551370253039,
            "R2": 0.6822557197544588,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.4194319999999999
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.300130820443067,
            "RMSE": 18.038310133249198,
            "R2": 0.7131646675929553,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.4444929999999999
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.446939695127732,
            "RMSE": 18.13441953669637,
            "R2": 0.7364682185789984,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.4702589999999999
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.306713664516929,
            "RMSE": 19.446501901626007,
            "R2": 0.7057272396553849,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.4967349999999999
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.8047145381729,
            "RMSE": 20.530886427306594,
            "R2": 0.6984708214392588,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.523921
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.174415073298738,
            "RMSE": 21.133761140382827,
            "R2": 0.7173255769005842,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.551805
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.2883642577537,
            "RMSE": 21.10340115690396,
            "R2": 0.7371933225224319,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.580392
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 14.156717848187574,
            "RMSE": 22.549679209142333,
            "R2": 0.7210842693854467,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.6096860000000001
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 14.91944953335544,
            "RMSE": 23.967687063528587,
            "R2": 0.7042149845564116,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.6396860000000001
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 15.467166242517186,
            "RMSE": 24.886955839016704,
            "R2": 0.7166083213097005,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.6704000000000001
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 15.631989433801651,
            "RMSE": 24.954278611820005,
            "R2": 0.735240056765428,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.7018220000000001
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 16.140858755557055,
            "RMSE": 25.549476814516595,
            "R2": 0.7342580119275103,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.7339490000000001
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 17.234115417053438,
            "RMSE": 27.64913352119068,
            "R2": 0.7076854506057617,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.766781
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 18.0152369206823,
            "RMSE": 28.967470484053976,
            "R2": 0.7166844816496443,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.800319
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 18.33784663215877,
            "RMSE": 29.23326362096376,
            "R2": 0.727273146935064,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.834558
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 18.785497932712666,
            "RMSE": 29.755293652524703,
            "R2": 0.7342033839127224,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.86951
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 19.668627686193567,
            "RMSE": 31.19471320280161,
            "R2": 0.7163564282233008,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.90517
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 20.38947136061499,
            "RMSE": 32.18441644636668,
            "R2": 0.7150766748346216,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.941543
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 21.174247281712567,
            "RMSE": 33.375214332088184,
            "R2": 0.7245232875146275,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 0.978621
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 21.335113723003413,
            "RMSE": 33.369412847265615,
            "R2": 0.7359905254430201,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 1.016405
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 22.319908918673335,
            "RMSE": 34.98038586656285,
            "R2": 0.7188252208291055,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 1.054903
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.02102944586984,
            "RMSE": 35.899425045778656,
            "R2": 0.7168073485461736,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 1.094104
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.86795045847124,
            "RMSE": 37.077313876148,
            "R2": 0.7205745757906983,
            "Memory in Mb": 0.0044412612915039,
            "Time in s": 1.134008
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 23.431235633428948,
            "RMSE": 26.218144216470428,
            "R2": -1611.3462157506035,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.004147
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 14.103513545807008,
            "RMSE": 19.087149489688155,
            "R2": -145.46960290724672,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.010783
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 11.461367198760032,
            "RMSE": 16.23222714650599,
            "R2": -141.81258639462544,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.018889
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 9.44127715126052,
            "RMSE": 14.201674320759096,
            "R2": -108.65615123709478,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.028452
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 7.797022024035496,
            "RMSE": 12.721240349043525,
            "R2": -54.205539694816935,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.039551
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 6.691147023027369,
            "RMSE": 11.629122321270428,
            "R2": -38.13701304656029,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.052122
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 5.831783229321132,
            "RMSE": 10.770680162674168,
            "R2": -33.69279126993988,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.066155
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 5.153144449790517,
            "RMSE": 10.076741978726949,
            "R2": -25.77937886024605,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.08166
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.653806702754108,
            "RMSE": 9.504457154537077,
            "R2": -19.92363756907144,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.098629
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.222103651464603,
            "RMSE": 9.017588926226493,
            "R2": -17.890910704295415,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.117152
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.8867321432249606,
            "RMSE": 8.600346446062781,
            "R2": -17.535660715889627,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.137154
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.599340946609919,
            "RMSE": 8.235553698215059,
            "R2": -16.124474758948196,
            "Memory in Mb": 0.0050439834594726,
            "Time in s": 0.15861
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.3420538385748757,
            "RMSE": 7.912854669167724,
            "R2": -15.021792727856036,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.181525
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.121876705697044,
            "RMSE": 7.625390851691296,
            "R2": -14.577959242562436,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.205897
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.9443386382725367,
            "RMSE": 7.3683114276631025,
            "R2": -13.30448388815742,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.231796
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.815755936756583,
            "RMSE": 7.138230019587049,
            "R2": -13.089830522149688,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.259173
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.6933833627330244,
            "RMSE": 6.928597052658441,
            "R2": -13.027805837336182,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.288012
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.6051143953909115,
            "RMSE": 6.739167122054826,
            "R2": -12.380223856378365,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.318313
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.490520088621087,
            "RMSE": 6.560408055638074,
            "R2": -12.118440379947032,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.350072
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.379600080775968,
            "RMSE": 6.3947378153227445,
            "R2": -11.816514349639151,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.383345
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.2783211278818065,
            "RMSE": 6.240996339547436,
            "R2": -11.61166202267384,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.418092
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.2145782025697205,
            "RMSE": 6.101000859547544,
            "R2": -10.83412932108482,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.454298
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.1464112051078263,
            "RMSE": 5.968705291729145,
            "R2": -9.740869666058233,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.491959
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.072454283271577,
            "RMSE": 5.843773480387036,
            "R2": -9.059069500744918,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.5310900000000001
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.9987939253418097,
            "RMSE": 5.726023081885353,
            "R2": -8.45516263823347,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.5716870000000001
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.9284894530733132,
            "RMSE": 5.614979238753044,
            "R2": -8.107866604370331,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.613828
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.8708966196370944,
            "RMSE": 5.510640598064868,
            "R2": -7.740375491210358,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.657455
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.824494929332068,
            "RMSE": 5.412971505312132,
            "R2": -7.634241934578528,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.702504
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.781951127238344,
            "RMSE": 5.3203622791847724,
            "R2": -7.547628985954546,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.748994
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.749732390051898,
            "RMSE": 5.233421242207161,
            "R2": -7.179064952823026,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.796981
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.7052484400139905,
            "RMSE": 5.14921027958835,
            "R2": -6.797272491389374,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.846385
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.6664817162996513,
            "RMSE": 5.068963198399273,
            "R2": -6.414896594696412,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.897251
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.6214900718153242,
            "RMSE": 4.99171743637858,
            "R2": -6.138924064419633,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 0.949568
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.5818233283584242,
            "RMSE": 4.918048415051679,
            "R2": -6.03927170869104,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.003319
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.555259840641907,
            "RMSE": 4.848763195223404,
            "R2": -6.02204294951599,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.058593
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.532054525069809,
            "RMSE": 4.783346185353484,
            "R2": -5.983984772166844,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.1153050000000002
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.5146024654094865,
            "RMSE": 4.7215191517857305,
            "R2": -5.800515662606876,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.1734340000000003
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.4818289913711118,
            "RMSE": 4.659306491272199,
            "R2": -5.694229888242945,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.2330550000000002
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.452402157072035,
            "RMSE": 4.59956290700914,
            "R2": -5.552882667907455,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.294088
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.4293016341621465,
            "RMSE": 4.542852809132106,
            "R2": -5.450103306475059,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.356613
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.4031025761620075,
            "RMSE": 4.487566758646917,
            "R2": -5.363185739412862,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.420603
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.381369306663701,
            "RMSE": 4.43470615373713,
            "R2": -5.271853959037296,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.48601
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.3592027324075535,
            "RMSE": 4.3834303912536,
            "R2": -5.11710119981194,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.552867
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.3365452172324814,
            "RMSE": 4.3337346544721145,
            "R2": -4.949476248649982,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.621167
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.309932841675593,
            "RMSE": 4.285399956971287,
            "R2": -4.842022075269781,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.690888
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.286195364366444,
            "RMSE": 4.238743982476022,
            "R2": -4.809417914789597,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.762146
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.270754149650798,
            "RMSE": 4.194574036632911,
            "R2": -4.737236102715975,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.834847
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.252007480522268,
            "RMSE": 4.151199175197265,
            "R2": -4.677947706919012,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.908959
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.2327553756112288,
            "RMSE": 4.10900051997898,
            "R2": -4.671141158917876,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 1.984552
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Linear Regression with l1 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.2158544056174447,
            "RMSE": 4.0682125513101886,
            "R2": -4.652689174637866,
            "Memory in Mb": 0.0052042007446289,
            "Time in s": 2.061558
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 32.49979765090093,
            "RMSE": 33.085767570527814,
            "R2": -1408.093935143081,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.00221
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.548763427243948,
            "RMSE": 25.711783397814365,
            "R2": -699.1539821884553,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.0060149999999999
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 16.994606748791693,
            "RMSE": 21.16216382986949,
            "R2": -310.0297747454571,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.010773
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.434663043069094,
            "RMSE": 18.386175360023177,
            "R2": -265.1519301746234,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.016452
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.685726760044922,
            "RMSE": 18.64479618798502,
            "R2": -66.86112450289035,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.023006
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.3059577367172,
            "RMSE": 17.58876192176611,
            "R2": -25.03287862681572,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.030252
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.844694328458631,
            "RMSE": 16.6807536659431,
            "R2": -14.693178357367543,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.03818
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.154725738202892,
            "RMSE": 15.783555067193374,
            "R2": -11.739056703820452,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.046793
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.383929359740238,
            "RMSE": 14.970988963724652,
            "R2": -8.585892537614809,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.056087
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.96579366260941,
            "RMSE": 14.36848414897767,
            "R2": -5.166041463970149,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.066275
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.69456937849415,
            "RMSE": 13.920059192886765,
            "R2": -3.4570517192093604,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.077161
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.550940690791585,
            "RMSE": 13.540299798742517,
            "R2": -2.4466881997122822,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.088733
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.359343163302276,
            "RMSE": 13.17888693683795,
            "R2": -1.6446630191344274,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.100994
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.050096583806178,
            "RMSE": 12.809003240652473,
            "R2": -1.1232058766616235,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.113939
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.0176805612097,
            "RMSE": 12.690905771048246,
            "R2": -0.6754526017728211,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.127575
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.128420828629457,
            "RMSE": 12.67565049026222,
            "R2": -0.3476766887041909,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.141896
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.200055067293626,
            "RMSE": 12.61943948921252,
            "R2": -0.0936676208508318,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.156913
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.131920516304556,
            "RMSE": 12.48608852319409,
            "R2": 0.14832986501041,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.172621
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.262178084838377,
            "RMSE": 12.632807163510387,
            "R2": 0.2813122010719644,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.18901
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.624585089266471,
            "RMSE": 13.14522964439942,
            "R2": 0.3187088278286061,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.206079
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 9.871229105762628,
            "RMSE": 13.33182219595452,
            "R2": 0.4005868940419749,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.223824
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.053594156641497,
            "RMSE": 13.615837484576032,
            "R2": 0.496913232046656,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.242255
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.103586276318884,
            "RMSE": 13.654347763291469,
            "R2": 0.5605873283913356,
            "Memory in Mb": 0.0041532516479492,
            "Time in s": 0.261365
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 10.539757430756955,
            "RMSE": 14.361033144769577,
            "R2": 0.5558923432468688,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.281177
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.000663746720075,
            "RMSE": 15.253690514733572,
            "R2": 0.5591184315358017,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.301675
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.301045102393736,
            "RMSE": 15.716738058687294,
            "R2": 0.5946085911267809,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.32286
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.275670942063872,
            "RMSE": 15.722526759958118,
            "R2": 0.648148884657232,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.344736
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 11.737413962135747,
            "RMSE": 16.425717512690383,
            "R2": 0.6579773485389515,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.367308
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 12.62956768598283,
            "RMSE": 18.5239816734196,
            "R2": 0.6052658886851463,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.390571
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.20835169207171,
            "RMSE": 19.400144953397177,
            "R2": 0.6294827674482892,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.41452
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.34580485099439,
            "RMSE": 19.47322215763284,
            "R2": 0.6657152345574865,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.439156
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 13.572829398695534,
            "RMSE": 19.644456145190084,
            "R2": 0.6907528542453616,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.464482
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 14.286348966120116,
            "RMSE": 20.694687599962585,
            "R2": 0.666738740088638,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.490494
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 14.777113556436731,
            "RMSE": 21.8206517710938,
            "R2": 0.6593962849465681,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.517211
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 15.215863000720542,
            "RMSE": 22.583610768099227,
            "R2": 0.6772102871974224,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.544615
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 15.33144965807796,
            "RMSE": 22.564695888148663,
            "R2": 0.6995373757169706,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.5727059999999999
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 16.156138146741625,
            "RMSE": 23.924755047114477,
            "R2": 0.6860306363812331,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.601482
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 16.826141311926307,
            "RMSE": 25.281544830782227,
            "R2": 0.6708975363085852,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.6309469999999999
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 17.40263926327312,
            "RMSE": 26.38004441662919,
            "R2": 0.6815842184892376,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.6611069999999999
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 17.533400796677356,
            "RMSE": 26.42712307382207,
            "R2": 0.7030645738539452,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.6919729999999998
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 18.01931805998843,
            "RMSE": 26.98764790902567,
            "R2": 0.7034989551644695,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.7235269999999998
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 19.02005973582853,
            "RMSE": 28.983219342716676,
            "R2": 0.6787962347144068,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.7557739999999998
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 19.888963224686226,
            "RMSE": 30.578078926209333,
            "R2": 0.6843036130043219,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.7887069999999998
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 20.14556805064173,
            "RMSE": 30.710181129007665,
            "R2": 0.6990197135707891,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.8223269999999998
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 20.606054171923702,
            "RMSE": 31.270986299633183,
            "R2": 0.7064351021760091,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.8566339999999998
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 21.410220326067677,
            "RMSE": 32.615082621422005,
            "R2": 0.6899384474766328,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.8916409999999998
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 22.149063292155795,
            "RMSE": 33.66176418126127,
            "R2": 0.6883188968774838,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.9273449999999998
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 22.923596011881333,
            "RMSE": 34.92960124509041,
            "R2": 0.6982661596564212,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 0.9637369999999996
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.042465823580866,
            "RMSE": 34.93124976178739,
            "R2": 0.7106985365247873,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 1.0008159999999997
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 23.974366627279803,
            "RMSE": 36.47485289150521,
            "R2": 0.6942867450600009,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 1.0385829999999998
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 24.688352372874245,
            "RMSE": 37.45551228620605,
            "R2": 0.6917248794696187,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 1.077041
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "ChickWeights",
            "MAE": 25.52040552278537,
            "RMSE": 38.65530944983144,
            "R2": 0.6962839796503111,
            "Memory in Mb": 0.0042333602905273,
            "Time in s": 1.116183
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 23.51586240468561,
            "RMSE": 26.237375459551668,
            "R2": -1613.712423965852,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.004083
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 14.404588626352648,
            "RMSE": 19.15618772462805,
            "R2": -146.53108046561562,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.01063
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 12.231791081689297,
            "RMSE": 16.474815193156783,
            "R2": -146.113106004694,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.018597
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 9.897294138330498,
            "RMSE": 14.380930849374858,
            "R2": -111.44182781593445,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.027966
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 8.086918618304638,
            "RMSE": 12.871841233853624,
            "R2": -55.52038254270653,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.038819
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 7.090525087262731,
            "RMSE": 11.800543733353924,
            "R2": -39.29933105483862,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.051073
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 6.252895179240796,
            "RMSE": 10.939748534807466,
            "R2": -34.79049149741283,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.064731
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 5.613172563674658,
            "RMSE": 10.244365728872303,
            "R2": -26.67772385659461,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.079792
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 5.139122523864994,
            "RMSE": 9.674573881172426,
            "R2": -20.679349421494624,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.096247
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.970287512907828,
            "RMSE": 9.286148634805688,
            "R2": -19.03287536608377,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.114161
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.714509288646119,
            "RMSE": 8.88589717245386,
            "R2": -18.78694495096694,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.133481
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.3785831664508095,
            "RMSE": 8.51169894931726,
            "R2": -17.292125083299812,
            "Memory in Mb": 0.004836082458496,
            "Time in s": 0.154212
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.192432902948977,
            "RMSE": 8.203158141559566,
            "R2": -16.21895925323482,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.176332
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 4.032216676138626,
            "RMSE": 7.92689648751503,
            "R2": -15.834209174335763,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.199865
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.888249411356283,
            "RMSE": 7.680244711632193,
            "R2": -14.54126486396457,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.224857
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.851910342336546,
            "RMSE": 7.48583024126048,
            "R2": -14.495465984230798,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.251273
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.7628843932429423,
            "RMSE": 7.2990742240635536,
            "R2": -14.5680671641431,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.279095
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.741498329747232,
            "RMSE": 7.147194018854174,
            "R2": -14.04949995366026,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.308317
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.6331417160345065,
            "RMSE": 6.972318267910069,
            "R2": -13.817498979914417,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.3389480000000001
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.505723677240456,
            "RMSE": 6.801269751447825,
            "R2": -13.497878046830476,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.371039
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.377789937544477,
            "RMSE": 6.6406714986639335,
            "R2": -13.278693194916952,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.4045350000000001
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.285565585155429,
            "RMSE": 6.496417025168413,
            "R2": -12.417819031510929,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.4394350000000001
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.204438206990859,
            "RMSE": 6.363151879091182,
            "R2": -11.207416254643826,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.4757300000000001
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.1147239220792944,
            "RMSE": 6.234124280033156,
            "R2": -10.44779843680249,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.5134280000000001
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 3.0674610457420317,
            "RMSE": 6.126558214637352,
            "R2": -9.824203383261038,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.5525380000000001
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.990407253638538,
            "RMSE": 6.01302433311803,
            "R2": -9.444947809169491,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.593122
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.9353658306947947,
            "RMSE": 5.909270916056388,
            "R2": -9.05064000964308,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.635128
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.8633890512526734,
            "RMSE": 5.806679023039649,
            "R2": -8.935926541145857,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.6785490000000001
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.807495338487497,
            "RMSE": 5.711109374041071,
            "R2": -8.849273711490637,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.723357
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.7371272959787114,
            "RMSE": 5.616984296672238,
            "R2": -8.421904346026553,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.769575
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.695279458158905,
            "RMSE": 5.533794104458184,
            "R2": -8.005492094038127,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.817237
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.663427445960627,
            "RMSE": 5.457208108806078,
            "R2": -7.594247452705627,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.866263
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.616152871221604,
            "RMSE": 5.378587544649896,
            "R2": -7.28837246231315,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.916653
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.5798661012588893,
            "RMSE": 5.305972052989116,
            "R2": -7.193548818831784,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 0.968481
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.537320459903927,
            "RMSE": 5.236098928386573,
            "R2": -7.188742583674767,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.021719
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.487562037475977,
            "RMSE": 5.165214649048708,
            "R2": -7.14359946989749,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.076348
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.4359344014471898,
            "RMSE": 5.096521995605296,
            "R2": -6.923665614900413,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.1323770000000002
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.407655610747697,
            "RMSE": 5.035258504842907,
            "R2": -6.818106944929671,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.1897670000000002
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.359216458068109,
            "RMSE": 4.971257259303496,
            "R2": -6.65476288050581,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.2485520000000003
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.316070029510264,
            "RMSE": 4.9101929612142525,
            "R2": -6.535402552442101,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.3087800000000005
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.2777366252623445,
            "RMSE": 4.852446886619337,
            "R2": -6.440024000118236,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.3703650000000005
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.243368105900121,
            "RMSE": 4.7970088928814505,
            "R2": -6.33849981001193,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.4333480000000005
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.208161873346368,
            "RMSE": 4.742699334581194,
            "R2": -6.1609167229990645,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.4977110000000002
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.173524312605847,
            "RMSE": 4.690026300839657,
            "R2": -5.967944096931786,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.5634250000000005
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.143113317062195,
            "RMSE": 4.639957881226245,
            "R2": -5.848706397355668,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.6305320000000003
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.107662636673197,
            "RMSE": 4.590154711256589,
            "R2": -5.812600067991807,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.6990770000000004
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.084055644614135,
            "RMSE": 4.5438188766398575,
            "R2": -5.732386133187966,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.7689810000000004
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.0573225686306618,
            "RMSE": 4.498049663013517,
            "R2": -5.666421016566231,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.8402960000000004
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 2.029372876222096,
            "RMSE": 4.453478872426294,
            "R2": -5.661880798559547,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.9129870000000004
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Linear Regression with l2 regularization",
            "dataset": "TrumpApproval",
            "MAE": 1.9991816433402003,
            "RMSE": 4.409973662813209,
            "R2": -5.642320489885111,
            "Memory in Mb": 0.0049962997436523,
            "Time in s": 1.9870360000000005
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 29.34636433128918,
            "RMSE": 30.877867366178624,
            "R2": -1226.303892160441,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.002755
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 16.78579478575624,
            "RMSE": 22.219906445728544,
            "R2": -521.8939460594183,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.007689
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 12.764406226748012,
            "RMSE": 18.43476392899385,
            "R2": -235.02444355689545,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0139269999999999
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 10.51475037374614,
            "RMSE": 16.140786164803156,
            "R2": -204.11441945614396,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.021043
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 11.118868381910096,
            "RMSE": 17.807152193193623,
            "R2": -60.900579144648304,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0290209999999999
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 10.068652098820438,
            "RMSE": 16.444921319285292,
            "R2": -21.75701273895947,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.037852
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 9.238561614797426,
            "RMSE": 15.414518181428049,
            "R2": -12.40107017683018,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0475289999999999
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 8.397438800335843,
            "RMSE": 14.475112340817043,
            "R2": -9.714489831884093,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0580659999999999
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.833048644024143,
            "RMSE": 13.715858800506394,
            "R2": -7.045954767890709,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.069447
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.655503029296072,
            "RMSE": 13.224205829308971,
            "R2": -4.223044606682061,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0819039999999999
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.616633860178707,
            "RMSE": 12.86945366769748,
            "R2": -2.809655727072758,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.0952199999999999
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.226514673025618,
            "RMSE": 12.359535435581538,
            "R2": -1.871770505407636,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1094009999999999
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.028644030968596,
            "RMSE": 11.955222747545204,
            "R2": -1.1763474084194208,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1244559999999999
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 6.986848640780892,
            "RMSE": 11.69340351574852,
            "R2": -0.7694704308339801,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1403709999999999
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.055944609610511,
            "RMSE": 11.647997480703344,
            "R2": -0.411397823157807,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1571089999999999
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.165300854035116,
            "RMSE": 11.69334605191042,
            "R2": -0.146892755517725,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1746439999999999
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.086580322778478,
            "RMSE": 11.479257625599036,
            "R2": 0.0950328202686906,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.1929879999999999
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.0079421524022685,
            "RMSE": 11.279628541389028,
            "R2": 0.3049625679809165,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.2121359999999999
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.136281210496879,
            "RMSE": 11.437970564343969,
            "R2": 0.4108328996032877,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.2320939999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.591733813835971,
            "RMSE": 12.23821647621677,
            "R2": 0.409482641430799,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.252837
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.63642424272378,
            "RMSE": 12.197368986664095,
            "R2": 0.4982590675647103,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.274371
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.775639220351206,
            "RMSE": 12.334191292520584,
            "R2": 0.5871659255406134,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.296703
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 7.787415018822619,
            "RMSE": 12.26821713761009,
            "R2": 0.6452735558950271,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.31983
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 8.387229506824328,
            "RMSE": 13.12794439290609,
            "R2": 0.6288834273883384,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.343762
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 8.893165599265544,
            "RMSE": 14.22060275652947,
            "R2": 0.6168153604937621,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.368493
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 9.145334455404228,
            "RMSE": 14.488680433063887,
            "R2": 0.6554856011642076,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.394025
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 9.138984650870034,
            "RMSE": 14.40937364029996,
            "R2": 0.7044680409221951,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.420371
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 9.653721426872565,
            "RMSE": 15.186897141025446,
            "R2": 0.7076222812215553,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.447515
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 10.688547371510406,
            "RMSE": 17.568442046558065,
            "R2": 0.6449394075517852,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.475457
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 11.136888804773204,
            "RMSE": 18.130051576409294,
            "R2": 0.6764089203981734,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.5041950000000001
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 11.389709627918275,
            "RMSE": 18.31814497212097,
            "R2": 0.7041960757214223,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.53373
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 11.506556624125665,
            "RMSE": 18.357319157972537,
            "R2": 0.7299499902857889,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.56408
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 12.507799925411486,
            "RMSE": 19.94157204039453,
            "R2": 0.6905532928077196,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.5952430000000001
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 13.00643913732256,
            "RMSE": 20.915910426515573,
            "R2": 0.6870553798396234,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.6272240000000001
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 13.44126440090726,
            "RMSE": 21.59107831138786,
            "R2": 0.7049595304644938,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.6600050000000001
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 13.452600873244052,
            "RMSE": 21.4799043653453,
            "R2": 0.7277322681469997,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.6935880000000001
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 14.30954893105116,
            "RMSE": 22.795153034451378,
            "R2": 0.7149787127692513,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.7279810000000001
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 15.058465273046648,
            "RMSE": 24.12824896117789,
            "R2": 0.7002387244037227,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.7631730000000001
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 15.61316127520364,
            "RMSE": 25.00709438423813,
            "R2": 0.7138656442877266,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.799166
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 15.833192306896644,
            "RMSE": 25.159785721055627,
            "R2": 0.7308613212218023,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.8359580000000001
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 16.36714766376461,
            "RMSE": 25.770608582556893,
            "R2": 0.729638089688956,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.87355
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 17.39003054773241,
            "RMSE": 27.77320733878432,
            "R2": 0.7050560764454472,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.911945
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 18.288428268963266,
            "RMSE": 29.396681708172505,
            "R2": 0.7082265052542642,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.951137
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 18.65703381705754,
            "RMSE": 29.64739580601693,
            "R2": 0.7194912595024185,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.991127
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 19.170202167844984,
            "RMSE": 30.22319045197901,
            "R2": 0.7257784495510498,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.031919
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 20.00164363454025,
            "RMSE": 31.52072905752619,
            "R2": 0.7103967314785831,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.073505
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 20.7279777099298,
            "RMSE": 32.51187613530653,
            "R2": 0.7092492864364832,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.115928
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 21.56683033620196,
            "RMSE": 33.84128388534863,
            "R2": 0.7167757554755416,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.159144
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 21.76383497583081,
            "RMSE": 33.92033428284125,
            "R2": 0.727201090633804,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.203152
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 22.69913149057359,
            "RMSE": 35.42417858076478,
            "R2": 0.7116454901231712,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.247925
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 23.377380034069706,
            "RMSE": 36.32705612571005,
            "R2": 0.7100204288247138,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.293462
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "ChickWeights",
            "MAE": 24.23392939046311,
            "RMSE": 37.557568322570944,
            "R2": 0.7132890208408607,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.339772
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 19.88769754963664,
            "RMSE": 24.32970381980572,
            "R2": -1387.4429851591376,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.004188
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 13.670966252574736,
            "RMSE": 18.65150015508889,
            "R2": -138.85979610511808,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.011118
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 10.92834996141842,
            "RMSE": 15.667746469337834,
            "R2": -132.052589810652,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.019635
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 9.678171261463673,
            "RMSE": 14.124417656525663,
            "R2": -107.46634425227307,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.0297069999999999
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 9.352313294103828,
            "RMSE": 13.38210191485773,
            "R2": -60.090321390572015,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.041437
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 8.620142702346234,
            "RMSE": 12.447697479286916,
            "R2": -43.84064485890953,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.05473
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 8.069393725677067,
            "RMSE": 11.747669450243144,
            "R2": -40.272086023690846,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.069574
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 7.915997483818508,
            "RMSE": 11.323556682786094,
            "R2": -32.81628847194888,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.085987
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 7.901057285338727,
            "RMSE": 11.048721851620664,
            "R2": -27.27526182903414,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.103947
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 7.54356570823564,
            "RMSE": 10.615481381947994,
            "R2": -25.17890116869019,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.1235479999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 7.241521693861677,
            "RMSE": 10.231227443733497,
            "R2": -25.232015334984823,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.1447119999999999
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 7.008192421558015,
            "RMSE": 9.935910620042463,
            "R2": -23.925679436807183,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.1674199999999999
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 6.801990869552961,
            "RMSE": 9.666795781283112,
            "R2": -22.91166502123009,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.191681
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 6.624313646675292,
            "RMSE": 9.422664085622769,
            "R2": -22.786676328633025,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.217492
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 6.459069309379183,
            "RMSE": 9.212027904845302,
            "R2": -21.358709628275356,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.244937
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 6.271769455500056,
            "RMSE": 8.978276576497144,
            "R2": -21.290029949269996,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.2739479999999999
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 6.106653016686588,
            "RMSE": 8.760106381933458,
            "R2": -21.42424847489592,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.304509
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.987363514041657,
            "RMSE": 8.573066448421043,
            "R2": -20.653260781415117,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.336642
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.8616356212919145,
            "RMSE": 8.393806584529749,
            "R2": -20.475259224624704,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.370328
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.709779552257037,
            "RMSE": 8.216191215364908,
            "R2": -20.15755692495403,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.4056389999999999
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.611842526965273,
            "RMSE": 8.072589482864162,
            "R2": -20.100376445858966,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.442509
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.621266668644241,
            "RMSE": 8.061169250733263,
            "R2": -19.659995268253144,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.480923
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.589374981160082,
            "RMSE": 7.977922595195435,
            "R2": -18.1892858176961,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.520896
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.601949193869223,
            "RMSE": 7.939757215258646,
            "R2": -17.568871361729258,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.5624170000000001
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.5323381947357735,
            "RMSE": 7.827118471157092,
            "R2": -16.667155417363553,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.6055100000000001
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.482642323931563,
            "RMSE": 7.735647602994712,
            "R2": -16.286764124140948,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.6502260000000001
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.40625682094428,
            "RMSE": 7.63238246035087,
            "R2": -15.7666448554263,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.696447
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.339029679572209,
            "RMSE": 7.532223621796607,
            "R2": -15.718570546376949,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.744222
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.278136676956568,
            "RMSE": 7.444054065699633,
            "R2": -15.733326658615429,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.7935180000000001
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.267448053107655,
            "RMSE": 7.406286860836784,
            "R2": -15.380732931295814,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.8443630000000001
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.236749685364014,
            "RMSE": 7.349650271122191,
            "R2": -14.88527744664384,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.8968030000000001
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.212060707085285,
            "RMSE": 7.303465599867649,
            "R2": -14.393054201831111,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.95074
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.169763730821092,
            "RMSE": 7.239859498572405,
            "R2": -14.017341318649356,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.0062160000000002
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.126488999027155,
            "RMSE": 7.167741867944588,
            "R2": -13.952260083042017,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.063227
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.093088048073085,
            "RMSE": 7.110044108134988,
            "R2": -14.098928285386927,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.121789
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.090740367293551,
            "RMSE": 7.074302078930798,
            "R2": -14.275901824522656,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.181923
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.094807885255693,
            "RMSE": 7.045283722404726,
            "R2": -14.141723406350016,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.243554
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.043787658869922,
            "RMSE": 6.975646542541488,
            "R2": -14.00468895273832,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.306712
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.064043270517397,
            "RMSE": 6.970645877797938,
            "R2": -14.050305184338798,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.3714110000000002
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.100755566375936,
            "RMSE": 7.010389089224324,
            "R2": -14.360083784619212,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.4376520000000002
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.088064827359337,
            "RMSE": 6.979627415872227,
            "R2": -14.392786134873418,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.505445
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.068856460674791,
            "RMSE": 6.93736545783203,
            "R2": -14.348127111309871,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.574755
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.054699520351681,
            "RMSE": 6.900248160625591,
            "R2": -14.158172906563095,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.645553
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.051365258335469,
            "RMSE": 6.881479694679562,
            "R2": -14.000915574481752,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.717914
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 5.025346349320704,
            "RMSE": 6.842894221251935,
            "R2": -13.895672840614656,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.791764
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 4.9962011230931616,
            "RMSE": 6.800765764747934,
            "R2": -13.95456831471299,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.867216
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 4.964612353038952,
            "RMSE": 6.764345134580912,
            "R2": -13.920332812605436,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.944198
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 4.9296416909632255,
            "RMSE": 6.717192667284049,
            "R2": -13.866880687662514,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.02269
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 4.910978624057615,
            "RMSE": 6.682715130965835,
            "R2": -14.000438748691009,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.102738
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 1",
            "dataset": "TrumpApproval",
            "MAE": 4.906394390750375,
            "RMSE": 6.665596501187553,
            "R2": -14.174901311798424,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.184247
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 40.361343182089286,
            "RMSE": 50.93510711941157,
            "R2": -3338.580868182736,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.003338
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 33.77268754890631,
            "RMSE": 41.67984599422324,
            "R2": -1838.845575618055,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.00919
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 32.39258875507137,
            "RMSE": 38.96806999674433,
            "R2": -1053.6287703611629,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.01639
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 30.94881031854868,
            "RMSE": 36.76152485506615,
            "R2": -1062.9809670274265,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.024921
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 33.955857035779495,
            "RMSE": 41.369655851763525,
            "R2": -333.094700988151,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.034827
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 34.010493836145145,
            "RMSE": 40.92418807176112,
            "R2": -139.93270784533922,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.046059
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 34.064338631511326,
            "RMSE": 40.5595538563462,
            "R2": -91.78246602216656,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.058629
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 34.363478110253816,
            "RMSE": 40.47408671194747,
            "R2": -82.76869054449229,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.072516
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 34.108671766629826,
            "RMSE": 39.953033914579606,
            "R2": -67.2701887367714,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.087732
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 35.5272246808861,
            "RMSE": 41.29414928968925,
            "R2": -49.9285816695273,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.104612
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 35.85052464333277,
            "RMSE": 41.48724749727828,
            "R2": -38.59084342971371,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.122819
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 36.414238795248615,
            "RMSE": 42.10793271457587,
            "R2": -32.332913655998325,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.142364
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 37.27092918309872,
            "RMSE": 43.0841670883325,
            "R2": -27.26495387953688,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.163229
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 37.68834060456834,
            "RMSE": 43.351809236536255,
            "R2": -23.3206899065102,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.18538
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 37.63751931524077,
            "RMSE": 43.32469674855668,
            "R2": -18.52621065458175,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.208847
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 38.77878602757167,
            "RMSE": 44.74953718825682,
            "R2": -15.796635622291838,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.233634
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 39.47954967522975,
            "RMSE": 45.39032172466195,
            "R2": -13.149195443978996,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.259707
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 40.91548075261064,
            "RMSE": 46.96428169788168,
            "R2": -11.049082215962626,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.287109
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 41.53723737741547,
            "RMSE": 47.716579905431935,
            "R2": -9.253665706385002,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.31584
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 41.99935380922626,
            "RMSE": 48.63121942098776,
            "R2": -8.324525171754294,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.345843
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 42.76794868726854,
            "RMSE": 49.65880643089243,
            "R2": -7.316484115890946,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.377141
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 44.368299619960766,
            "RMSE": 51.88245138837915,
            "R2": -6.304578357179455,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.409767
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 45.426835880148886,
            "RMSE": 53.192808855117775,
            "R2": -5.668628208432534,
            "Memory in Mb": 0.0034055709838867,
            "Time in s": 0.443674
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 46.93737170570451,
            "RMSE": 55.9021194350506,
            "R2": -5.729354993233594,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.478844
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 48.507353400069945,
            "RMSE": 58.8434937271261,
            "R2": -5.560984055006233,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.515365
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 49.83788736782816,
            "RMSE": 60.74084767697289,
            "R2": -5.054961799673954,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.5532039999999999
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 51.62361105051165,
            "RMSE": 63.27455882125991,
            "R2": -4.698656745997159,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.5923289999999999
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 53.1847087657747,
            "RMSE": 65.32139627595005,
            "R2": -4.409001340116382,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.6328059999999999
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 55.18568520771326,
            "RMSE": 70.36874449488667,
            "R2": -4.696335728503607,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.6746009999999999
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 56.89081675494835,
            "RMSE": 72.51519786174504,
            "R2": -4.176742159590063,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.7176629999999999
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 58.741890997125225,
            "RMSE": 75.13624143509449,
            "R2": -3.976681879584251,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.7620199999999999
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 60.2425190521958,
            "RMSE": 76.8261590755005,
            "R2": -3.729812475420129,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.8076819999999999
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 62.22918871806441,
            "RMSE": 80.45649530418282,
            "R2": -4.037201263859445,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.854609
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 64.15805403621584,
            "RMSE": 84.29062360683722,
            "R2": -4.082442538013045,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.902845
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 65.35464556519459,
            "RMSE": 85.58979700811152,
            "R2": -3.6363575203718743,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 0.952397
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 67.08652533638559,
            "RMSE": 87.70251677464411,
            "R2": -3.538952097004609,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.00322
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 68.34565949899115,
            "RMSE": 89.3540667816312,
            "R2": -3.3794635851122994,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.055319
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 70.95506872236689,
            "RMSE": 94.70758550832085,
            "R2": -3.618420231648276,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.108722
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 72.57879663609631,
            "RMSE": 96.822819417077,
            "R2": -3.2894241164712765,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.163438
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 74.40667828471298,
            "RMSE": 99.12463362784464,
            "R2": -3.1775863007897582,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.219419
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 75.93202948942836,
            "RMSE": 101.47969042740628,
            "R2": -3.192319994595937,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.276691
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 78.59712471455953,
            "RMSE": 106.68213481552291,
            "R2": -3.3518185198786687,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.335258
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 81.70573920737151,
            "RMSE": 112.24508574603004,
            "R2": -3.253866822086197,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.395089
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 82.72251416230137,
            "RMSE": 113.16810597159808,
            "R2": -3.0871576545332315,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.456215
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 84.44211178292737,
            "RMSE": 115.99711612480068,
            "R2": -3.039385949207989,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.518639
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 86.55149997089892,
            "RMSE": 119.94151559804617,
            "R2": -3.193242857597108,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.582321
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 87.81070722823603,
            "RMSE": 121.26627191062052,
            "R2": -3.0449837234699952,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.64731
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 90.44199567451936,
            "RMSE": 126.238673662019,
            "R2": -2.9411377147279807,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.713605
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 91.59067370330054,
            "RMSE": 127.24192286613216,
            "R2": -2.8386881284150203,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.781138
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 93.78609063040562,
            "RMSE": 130.999704877259,
            "R2": -2.943372518937519,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.84997
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 96.49865979675556,
            "RMSE": 135.93192637304293,
            "R2": -3.060223463970532,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.920139
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "ChickWeights",
            "MAE": 99.56805853722273,
            "RMSE": 141.40025114882988,
            "R2": -3.0639630782357843,
            "Memory in Mb": 0.0034589767456054,
            "Time in s": 1.991547
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 38.256966119949794,
            "RMSE": 53.46437671117289,
            "R2": -6703.762875072117,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.004258
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 36.86518407094958,
            "RMSE": 46.91757933405302,
            "R2": -883.9863015306486,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.0112559999999999
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 34.81538726709292,
            "RMSE": 43.77024226536395,
            "R2": -1037.408328049847,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.019887
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 32.82099099523828,
            "RMSE": 40.95636211937148,
            "R2": -911.003802678922,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.0300789999999999
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 32.41507697560151,
            "RMSE": 39.67328525303196,
            "R2": -535.9329715822871,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.041942
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 32.126533810299065,
            "RMSE": 38.74392424963554,
            "R2": -433.4111998192701,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.055368
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.578696449953306,
            "RMSE": 37.792227545537656,
            "R2": -426.12792465890055,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.070349
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.74326128631808,
            "RMSE": 36.75147996394125,
            "R2": -355.2131008927076,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.086898
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.01457804514465,
            "RMSE": 35.792387341570375,
            "R2": -295.7316609698654,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.104998
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.69358993814741,
            "RMSE": 35.287452593511624,
            "R2": -288.27615949420783,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.124741
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.653103799764548,
            "RMSE": 34.981694493871686,
            "R2": -305.6605175079266,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.146064
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.438535707776744,
            "RMSE": 34.575414655319626,
            "R2": -300.8328104705327,
            "Memory in Mb": 0.0043020248413085,
            "Time in s": 0.168934
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.47891951475184,
            "RMSE": 34.56744094622709,
            "R2": -304.7589578451177,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.193372
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.26309099262944,
            "RMSE": 34.21824031120625,
            "R2": -312.6907330516863,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.2193709999999999
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.22587791049338,
            "RMSE": 34.04470159277256,
            "R2": -304.37628668920115,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.246997
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.39018713755992,
            "RMSE": 34.027497016659055,
            "R2": -319.1729973057711,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.276184
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.42027037377748,
            "RMSE": 33.93053373578466,
            "R2": -335.4190027425263,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.306921
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.664307062669348,
            "RMSE": 34.045635299267715,
            "R2": -340.48671423689984,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.339233
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 29.83498723746747,
            "RMSE": 34.11808971579651,
            "R2": -353.80514851974,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.373101
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.001082895685222,
            "RMSE": 34.17628998525774,
            "R2": -365.0785427385626,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.408596
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.14554243966483,
            "RMSE": 34.20268208319664,
            "R2": -377.7780423674053,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.445652
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.318997649838,
            "RMSE": 34.29163258825692,
            "R2": -372.8612574130533,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.484259
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.44816166194883,
            "RMSE": 34.34474274542465,
            "R2": -354.6310813895727,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.524426
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.547707035634,
            "RMSE": 34.3460988289287,
            "R2": -346.476863625336,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.5661419999999999
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.677713278160866,
            "RMSE": 34.40102042286509,
            "R2": -340.27577766039445,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.6094289999999999
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.774567489967996,
            "RMSE": 34.41616981796676,
            "R2": -341.1727526506248,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.6543389999999999
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.8774276068303,
            "RMSE": 34.45885995564912,
            "R2": -340.7651110108783,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.7007559999999999
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.809160821418956,
            "RMSE": 34.35467967149731,
            "R2": -346.7959646189386,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.7487349999999999
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.794626934327955,
            "RMSE": 34.31319945532044,
            "R2": -354.5377185045104,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.798249
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 30.95165244409411,
            "RMSE": 34.41180694760753,
            "R2": -352.62847406429205,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.849322
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.05924245979316,
            "RMSE": 34.47559777081781,
            "R2": -348.53049085374005,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.901986
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.17486346702509,
            "RMSE": 34.55495775749415,
            "R2": -343.578007451748,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 0.956154
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.18138785276698,
            "RMSE": 34.53217565702543,
            "R2": -340.6493968041527,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.011873
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.262098564397714,
            "RMSE": 34.57860649898553,
            "R2": -346.98225985471817,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.06915
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.21351117376332,
            "RMSE": 34.56642775102796,
            "R2": -355.8704038677769,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.127995
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.187412408778744,
            "RMSE": 34.52480046664081,
            "R2": -362.8329367085535,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.188423
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.11951946368673,
            "RMSE": 34.44075758421072,
            "R2": -360.84595808308967,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.250358
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.06286774404838,
            "RMSE": 34.392033812715184,
            "R2": -363.7319274626152,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.313829
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.122129081397333,
            "RMSE": 34.4147077867913,
            "R2": -365.8490836115921,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.378848
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.106214253085103,
            "RMSE": 34.39160753515401,
            "R2": -368.6700713862459,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.445416
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.221689813214,
            "RMSE": 34.48240321448139,
            "R2": -374.7057202811433,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.513551
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.279425902447173,
            "RMSE": 34.50697415799086,
            "R2": -378.7344488771949,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.583215
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.342876956175303,
            "RMSE": 34.54160049479585,
            "R2": -378.8414458535583,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.65438
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.26946109805924,
            "RMSE": 34.463329541799936,
            "R2": -375.2431199026635,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.727121
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.252963502360984,
            "RMSE": 34.437602544585566,
            "R2": -376.2648040183398,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.801358
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.17140034618248,
            "RMSE": 34.35879469425013,
            "R2": -380.710483609337,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.877212
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.028682196255257,
            "RMSE": 34.23221645186374,
            "R2": -381.1175926718204,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 1.954607
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.091829199349828,
            "RMSE": 34.349474902309865,
            "R2": -387.76257537598985,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.033516
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.00094350988743,
            "RMSE": 34.303507421677764,
            "R2": -394.25294990859175,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.113994
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Passive-Aggressive Regressor, mode 2",
            "dataset": "TrumpApproval",
            "MAE": 31.128814077399102,
            "RMSE": 34.425663215951964,
            "R2": -403.7738674316034,
            "Memory in Mb": 0.0044355392456054,
            "Time in s": 2.195941
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 4.6439393939393945,
            "RMSE": 12.708027567111456,
            "R2": -206.8805289598106,
            "Memory in Mb": 0.007791519165039,
            "Time in s": 0.002301
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.7674242424242426,
            "RMSE": 9.021574170013263,
            "R2": -85.19732920009746,
            "Memory in Mb": 0.0116405487060546,
            "Time in s": 0.007035
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.366161616161617,
            "RMSE": 7.437810062008745,
            "R2": -37.42129411139464,
            "Memory in Mb": 0.0161724090576171,
            "Time in s": 0.013843
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.015530303030304,
            "RMSE": 6.463663489621867,
            "R2": -31.893061768560024,
            "Memory in Mb": 0.0202007293701171,
            "Time in s": 0.022662
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.2124242424242424,
            "RMSE": 6.080421054665558,
            "R2": -6.217272109648366,
            "Memory in Mb": 0.0243968963623046,
            "Time in s": 0.033503
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.280050505050505,
            "RMSE": 5.694858940322259,
            "R2": -1.7290883479828647,
            "Memory in Mb": 0.0287837982177734,
            "Time in s": 0.046733
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.61926406926407,
            "RMSE": 5.707950266794224,
            "R2": -0.8375532519268223,
            "Memory in Mb": 0.0331974029541015,
            "Time in s": 0.062616
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.530492424242425,
            "RMSE": 5.412982721609634,
            "R2": -0.4983072905775765,
            "Memory in Mb": 0.0375041961669921,
            "Time in s": 0.081466
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.4755892255892267,
            "RMSE": 5.17010990945742,
            "R2": -0.1432234574096695,
            "Memory in Mb": 0.0422878265380859,
            "Time in s": 0.103593
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 2.7716666666666683,
            "RMSE": 5.296236752390676,
            "R2": 0.1622405877971293,
            "Memory in Mb": 0.0433177947998046,
            "Time in s": 0.129424
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 3.180853994490359,
            "RMSE": 5.621206607854847,
            "R2": 0.2731837882445769,
            "Memory in Mb": 0.0438785552978515,
            "Time in s": 0.158775
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 3.3642676767676765,
            "RMSE": 5.706770043255583,
            "R2": 0.3877536814355664,
            "Memory in Mb": 0.0436267852783203,
            "Time in s": 0.191664
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 3.646736596736596,
            "RMSE": 5.919243012407738,
            "R2": 0.4664867393310171,
            "Memory in Mb": 0.0439319610595703,
            "Time in s": 0.228099
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 3.7550865800865783,
            "RMSE": 5.97572666401829,
            "R2": 0.537892640768072,
            "Memory in Mb": 0.0440692901611328,
            "Time in s": 0.268063
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 4.093838383838381,
            "RMSE": 6.488494998076776,
            "R2": 0.562039588096868,
            "Memory in Mb": 0.0446529388427734,
            "Time in s": 0.311593
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 4.458428030303029,
            "RMSE": 6.947478945595657,
            "R2": 0.5951448357515823,
            "Memory in Mb": 0.0446796417236328,
            "Time in s": 0.358632
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 4.792959001782529,
            "RMSE": 7.272258331212408,
            "R2": 0.6368016898131145,
            "Memory in Mb": 0.0447597503662109,
            "Time in s": 0.40948
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 5.229713804713803,
            "RMSE": 7.766788141562423,
            "R2": 0.6704650236153215,
            "Memory in Mb": 0.0442829132080078,
            "Time in s": 0.46388
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 5.61188197767145,
            "RMSE": 8.429860803311705,
            "R2": 0.6799768871245477,
            "Memory in Mb": 0.0443363189697265,
            "Time in s": 0.521779
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 6.048560606060604,
            "RMSE": 9.536044923225656,
            "R2": 0.6414638231876792,
            "Memory in Mb": 0.0443096160888671,
            "Time in s": 0.583178
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 6.582178932178929,
            "RMSE": 10.20324912411692,
            "R2": 0.648905367768132,
            "Memory in Mb": 0.0448932647705078,
            "Time in s": 0.6480619999999999
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 7.071418732782365,
            "RMSE": 10.928542055135823,
            "R2": 0.6759002976153703,
            "Memory in Mb": 0.0449466705322265,
            "Time in s": 0.7164429999999999
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 7.477799736495386,
            "RMSE": 11.323352624926212,
            "R2": 0.6978095597045382,
            "Memory in Mb": 0.045053482055664,
            "Time in s": 0.7883119999999999
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 7.970770202020199,
            "RMSE": 12.28335187867794,
            "R2": 0.6750992767833781,
            "Memory in Mb": 0.0446300506591796,
            "Time in s": 0.8636689999999999
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 8.55812121212121,
            "RMSE": 13.382565810664548,
            "R2": 0.6606476529151027,
            "Memory in Mb": 0.0446834564208984,
            "Time in s": 0.942555
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 9.054137529137526,
            "RMSE": 14.013384412631826,
            "R2": 0.6777181990167639,
            "Memory in Mb": 0.0448436737060546,
            "Time in s": 1.024953
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 9.468967452300786,
            "RMSE": 14.435360812541292,
            "R2": 0.7034011013652389,
            "Memory in Mb": 0.0454006195068359,
            "Time in s": 1.110877
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 9.90871212121212,
            "RMSE": 15.173853281638724,
            "R2": 0.7081243055691319,
            "Memory in Mb": 0.0454273223876953,
            "Time in s": 1.200187
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 10.713740856844304,
            "RMSE": 17.013635837866804,
            "R2": 0.6670107307192514,
            "Memory in Mb": 0.0455341339111328,
            "Time in s": 1.2928449999999998
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 11.460252525252525,
            "RMSE": 18.125243873896306,
            "R2": 0.6765805165314649,
            "Memory in Mb": 0.045083999633789,
            "Time in s": 1.388826
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 11.901710654936462,
            "RMSE": 18.5766916053512,
            "R2": 0.6957870549438744,
            "Memory in Mb": 0.0451908111572265,
            "Time in s": 1.488176
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 12.310464015151512,
            "RMSE": 18.922178666477887,
            "R2": 0.7130752857476492,
            "Memory in Mb": 0.0451641082763671,
            "Time in s": 1.591164
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 12.780394857667584,
            "RMSE": 19.823234941774256,
            "R2": 0.694215027528111,
            "Memory in Mb": 0.0456142425537109,
            "Time in s": 1.697605
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 13.344073083778964,
            "RMSE": 20.889730456192645,
            "R2": 0.6878383009059359,
            "Memory in Mb": 0.0456142425537109,
            "Time in s": 1.807438
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 13.830865800865798,
            "RMSE": 21.557316750546796,
            "R2": 0.7058815074667231,
            "Memory in Mb": 0.045694351196289,
            "Time in s": 1.920665
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 14.08051346801346,
            "RMSE": 21.615344438143325,
            "R2": 0.7242879119502419,
            "Memory in Mb": 0.0452175140380859,
            "Time in s": 2.037277
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 14.665069615069608,
            "RMSE": 22.79756192033108,
            "R2": 0.714918470135155,
            "Memory in Mb": 0.0452442169189453,
            "Time in s": 2.157231
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 15.362400318979262,
            "RMSE": 24.076729101709564,
            "R2": 0.7015174886253861,
            "Memory in Mb": 0.0457477569580078,
            "Time in s": 2.280525
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 15.914413364413358,
            "RMSE": 24.924104546372128,
            "R2": 0.7157616535295273,
            "Memory in Mb": 0.0458278656005859,
            "Time in s": 2.407192
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 16.21655303030303,
            "RMSE": 25.17906749713446,
            "R2": 0.730448642009748,
            "Memory in Mb": 0.0458545684814453,
            "Time in s": 2.537243
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 16.571359940872135,
            "RMSE": 25.529131814454708,
            "R2": 0.7346810631079229,
            "Memory in Mb": 0.0458812713623046,
            "Time in s": 2.670662
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 17.517063492063492,
            "RMSE": 27.45837911410348,
            "R2": 0.7117049574257082,
            "Memory in Mb": 0.0453777313232421,
            "Time in s": 2.807433
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 18.23357998590557,
            "RMSE": 28.586680380220997,
            "R2": 0.7240841374900429,
            "Memory in Mb": 0.0453510284423828,
            "Time in s": 2.947633
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 18.61876721763086,
            "RMSE": 29.038858036362505,
            "R2": 0.7308884346272555,
            "Memory in Mb": 0.0458812713623046,
            "Time in s": 3.0911699999999995
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 19.16138047138048,
            "RMSE": 29.754410032566323,
            "R2": 0.7342191699916846,
            "Memory in Mb": 0.0458812713623046,
            "Time in s": 3.2380789999999995
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 19.69344532279316,
            "RMSE": 30.658970587616192,
            "R2": 0.7260154404176653,
            "Memory in Mb": 0.0458545684814453,
            "Time in s": 3.388348
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 20.317762733720187,
            "RMSE": 31.53258587823862,
            "R2": 0.7265009007981393,
            "Memory in Mb": 0.0453777313232421,
            "Time in s": 3.541995
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 21.03841540404041,
            "RMSE": 32.63466371480821,
            "R2": 0.7366125677104822,
            "Memory in Mb": 0.0454311370849609,
            "Time in s": 3.699025
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 21.282900432900444,
            "RMSE": 32.8391739011002,
            "R2": 0.7443140702924032,
            "Memory in Mb": 0.0454044342041015,
            "Time in s": 3.859333
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 21.858333333333334,
            "RMSE": 33.61129662942374,
            "R2": 0.7404041745313898,
            "Memory in Mb": 0.0460147857666015,
            "Time in s": 4.022901
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 22.36307189542484,
            "RMSE": 34.18934989679706,
            "R2": 0.7431446126310046,
            "Memory in Mb": 0.0460681915283203,
            "Time in s": 4.189756
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "ChickWeights",
            "MAE": 22.904341491841496,
            "RMSE": 34.79445522931405,
            "R2": 0.7539238777546076,
            "Memory in Mb": 0.046121597290039,
            "Time in s": 4.359905
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 2.5579731333333355,
            "RMSE": 9.79490509533104,
            "R2": -224.0374880099697,
            "Memory in Mb": 0.0161190032958984,
            "Time in s": 0.00492
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 1.814472516666667,
            "RMSE": 6.975921914401759,
            "R2": -18.564491994995524,
            "Memory in Mb": 0.0286769866943359,
            "Time in s": 0.014556
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 1.386012811111112,
            "RMSE": 5.70893041508138,
            "R2": -16.665248891500116,
            "Memory in Mb": 0.0407314300537109,
            "Time in s": 0.029158
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 1.1425351583333334,
            "RMSE": 4.950945892995169,
            "R2": -12.326934431680348,
            "Memory in Mb": 0.0527858734130859,
            "Time in s": 0.04994
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 1.0609460066666667,
            "RMSE": 4.443635225860514,
            "R2": -5.735976224554387,
            "Memory in Mb": 0.065317153930664,
            "Time in s": 0.078368
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 1.0173975888888886,
            "RMSE": 4.080152828774464,
            "R2": -3.8177766328983793,
            "Memory in Mb": 0.0658702850341796,
            "Time in s": 0.115087
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.9499007047619044,
            "RMSE": 3.785073461941064,
            "R2": -3.284514427728187,
            "Memory in Mb": 0.0653667449951171,
            "Time in s": 0.160142
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.8997031916666666,
            "RMSE": 3.548063392436267,
            "R2": -2.320037309218333,
            "Memory in Mb": 0.0653667449951171,
            "Time in s": 0.213621
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.8894699925925924,
            "RMSE": 3.3651237174821174,
            "R2": -1.6229174672077478,
            "Memory in Mb": 0.0658702850341796,
            "Time in s": 0.275231
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.8368248133333331,
            "RMSE": 3.1964619940401167,
            "R2": -1.3736195901717156,
            "Memory in Mb": 0.0653667449951171,
            "Time in s": 0.3451079999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.7973693939393937,
            "RMSE": 3.051737973437425,
            "R2": -1.333837761501293,
            "Memory in Mb": 0.0653667449951171,
            "Time in s": 0.4231859999999999
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.7882918027777774,
            "RMSE": 2.9302063484469683,
            "R2": -1.1678441811700535,
            "Memory in Mb": 0.0658702850341796,
            "Time in s": 0.5093219999999999
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.756480287179487,
            "RMSE": 2.818118800540444,
            "R2": -1.032185390259123,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 0.603278
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.7152656523809521,
            "RMSE": 2.716213897230066,
            "R2": -0.9765794643185606,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 0.705058
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6924420288888888,
            "RMSE": 2.626670145740793,
            "R2": -0.8178051192110904,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 0.8148869999999999
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6685162833333335,
            "RMSE": 2.544831183351663,
            "R2": -0.7907817018280727,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 0.932496
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6729953196078432,
            "RMSE": 2.478015515638401,
            "R2": -0.7943500832815562,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 1.057867
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6574798574074076,
            "RMSE": 2.410620514027796,
            "R2": -0.7120191674014065,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 1.1910109999999998
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6458375333333335,
            "RMSE": 2.3511270035956984,
            "R2": -0.6848943678054311,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 1.3319119999999998
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6474776666666668,
            "RMSE": 2.299895164719867,
            "R2": -0.6578320154352482,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 1.4805999999999997
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6263061492063494,
            "RMSE": 2.245732257498697,
            "R2": -0.6329783328857519,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 1.6370479999999996
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6161101106060607,
            "RMSE": 2.196509834675512,
            "R2": -0.5339119919932027,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 1.8010919999999997
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.6114796710144929,
            "RMSE": 2.151899880839346,
            "R2": -0.3961217660875815,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 1.972734
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.595679659722222,
            "RMSE": 2.1075134371992843,
            "R2": -0.3083133320099125,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 2.151984
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5871453373333329,
            "RMSE": 2.067421382434369,
            "R2": -0.2325961934637197,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 2.338834
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5787837589743586,
            "RMSE": 2.029002666882104,
            "R2": -0.1892840306210153,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 2.533354
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5648130308641971,
            "RMSE": 1.991660903442925,
            "R2": -0.1417123847500625,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 2.735472
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5728799083333329,
            "RMSE": 1.964965242398572,
            "R2": -0.1377909554693113,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 2.945174
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5729694735632179,
            "RMSE": 1.9355227317321977,
            "R2": -0.1312531571152491,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 3.162675
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5633090777777773,
            "RMSE": 1.904172510525728,
            "R2": -0.0827915396879483,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 3.387869
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5627685010752685,
            "RMSE": 1.877938378401011,
            "R2": -0.0371083516253996,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 3.620659
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5527265229166664,
            "RMSE": 1.8490211996046173,
            "R2": 0.0133784354988776,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 3.861011
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5494711494949491,
            "RMSE": 1.8235613734746328,
            "R2": 0.0472618750543785,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 4.108899
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5450294392156858,
            "RMSE": 1.7983422134533726,
            "R2": 0.05878940572589,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 4.364357
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5469558666666661,
            "RMSE": 1.7765896178823126,
            "R2": 0.0572950833274868,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 4.627459
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.543456514814814,
            "RMSE": 1.7539567687409483,
            "R2": 0.0609744119033208,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 4.898124
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5378193549549544,
            "RMSE": 1.7312282531924004,
            "R2": 0.085703628915721,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 5.1763650000000005
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5339037666666662,
            "RMSE": 1.709797998783685,
            "R2": 0.0985374850173486,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 5.462206
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5278528008547004,
            "RMSE": 1.688590710651063,
            "R2": 0.116822375782677,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 5.755616
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5283612208333329,
            "RMSE": 1.6702821330140922,
            "R2": 0.1280551636806639,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 6.056664
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5218793715447149,
            "RMSE": 1.650734458460968,
            "R2": 0.1389919937119252,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 6.365303
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5164909984126979,
            "RMSE": 1.6320321449108954,
            "R2": 0.1505777025063954,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 6.681529
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5203083496124026,
            "RMSE": 1.617111920842916,
            "R2": 0.167474405637749,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 7.005502
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5169651212121207,
            "RMSE": 1.6004898524254525,
            "R2": 0.188553388101048,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 7.337010999999999
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5126542296296291,
            "RMSE": 1.583708561642625,
            "R2": 0.2021320849395992,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 7.676102999999999
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5104052702898545,
            "RMSE": 1.5679886127118026,
            "R2": 0.2050422348676139,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 8.022855999999999
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5051605113475173,
            "RMSE": 1.551953998854848,
            "R2": 0.2146112384044058,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 8.377156
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.5025567965277773,
            "RMSE": 1.5374441378201589,
            "R2": 0.2211695274632112,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 8.739002999999999
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.4982526563945573,
            "RMSE": 1.522650494486571,
            "R2": 0.2212491734260424,
            "Memory in Mb": 0.065500259399414,
            "Time in s": 9.108430999999998
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "k-Nearest Neighbors",
            "dataset": "TrumpApproval",
            "MAE": 0.4939745494666663,
            "RMSE": 1.5080707141004983,
            "R2": 0.2232321406133778,
            "Memory in Mb": 0.0660037994384765,
            "Time in s": 9.485458999999995
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 8.042756132756132,
            "RMSE": 17.336048579080593,
            "R2": -385.8634917094176,
            "Memory in Mb": 0.0165748596191406,
            "Time in s": 0.003293
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.456785613727984,
            "RMSE": 12.282422261556867,
            "R2": -158.770726389092,
            "Memory in Mb": 0.0181541442871093,
            "Time in s": 0.009578
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 3.4353973358733074,
            "RMSE": 10.07037651743448,
            "R2": -69.4325218162971,
            "Memory in Mb": 0.0234184265136718,
            "Time in s": 0.01815
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 2.736909422894262,
            "RMSE": 8.732393473100391,
            "R2": -59.03623058514604,
            "Memory in Mb": 0.0244712829589843,
            "Time in s": 0.029162
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 2.788577579622257,
            "RMSE": 8.074088551816661,
            "R2": -11.726025456653014,
            "Memory in Mb": 0.0313148498535156,
            "Time in s": 0.042723
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 3.395880085598137,
            "RMSE": 7.878422021930021,
            "R2": -4.223121571879303,
            "Memory in Mb": 0.0407905578613281,
            "Time in s": 0.0593589999999999
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 3.889526501621088,
            "RMSE": 7.800910386370324,
            "R2": -2.432180745921895,
            "Memory in Mb": 0.0471076965332031,
            "Time in s": 0.0796159999999999
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.072650698433535,
            "RMSE": 7.572197783925699,
            "R2": -1.9320509270116557,
            "Memory in Mb": 0.0528984069824218,
            "Time in s": 0.103875
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.410984939713907,
            "RMSE": 7.55185413515251,
            "R2": -1.439151418709002,
            "Memory in Mb": 0.0539512634277343,
            "Time in s": 0.132276
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.441558524813062,
            "RMSE": 7.364764038532391,
            "R2": -0.6199522309877294,
            "Memory in Mb": 0.0555305480957031,
            "Time in s": 0.164898
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.487290951327676,
            "RMSE": 7.260940155844585,
            "R2": -0.2126939871368238,
            "Memory in Mb": 0.0555305480957031,
            "Time in s": 0.201538
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.401729970486312,
            "RMSE": 7.0591187066650845,
            "R2": 0.0632010249038049,
            "Memory in Mb": 0.0555305480957031,
            "Time in s": 0.242248
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.303599977233167,
            "RMSE": 6.863829202938119,
            "R2": 0.2826256992169514,
            "Memory in Mb": 0.0560569763183593,
            "Time in s": 0.2871789999999999
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.247967976141752,
            "RMSE": 6.717580819449276,
            "R2": 0.4160344373982124,
            "Memory in Mb": 0.0560569763183593,
            "Time in s": 0.3361619999999999
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.525268599337025,
            "RMSE": 6.978492074792776,
            "R2": 0.493394283015475,
            "Memory in Mb": 0.0560569763183593,
            "Time in s": 0.3890969999999999
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.7434869323510185,
            "RMSE": 7.161143757518859,
            "R2": 0.5698598432460567,
            "Memory in Mb": 0.0565834045410156,
            "Time in s": 0.4460369999999999
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.817684977356876,
            "RMSE": 7.1877471099050325,
            "R2": 0.6451941261958376,
            "Memory in Mb": 0.0565834045410156,
            "Time in s": 0.5072089999999999
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 4.83667165494537,
            "RMSE": 7.176577259975889,
            "R2": 0.7186458480933114,
            "Memory in Mb": 0.0565834045410156,
            "Time in s": 0.5725709999999999
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 5.073405719834179,
            "RMSE": 7.569308518085582,
            "R2": 0.7419802486075263,
            "Memory in Mb": 0.0217466354370117,
            "Time in s": 0.645323
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 5.671396913729996,
            "RMSE": 8.67042326781336,
            "R2": 0.7036008152378226,
            "Memory in Mb": 0.0280637741088867,
            "Time in s": 0.719465
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 5.870013976865108,
            "RMSE": 8.892004937785565,
            "R2": 0.7333469233470653,
            "Memory in Mb": 0.0333280563354492,
            "Time in s": 0.7950900000000001
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 6.098410134572789,
            "RMSE": 9.27860472778795,
            "R2": 0.7663748869623117,
            "Memory in Mb": 0.0380659103393554,
            "Time in s": 0.8723510000000001
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 6.1962339865774,
            "RMSE": 9.406595007903094,
            "R2": 0.7914570321252903,
            "Memory in Mb": 0.0417509078979492,
            "Time in s": 0.951359
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 6.851942913488504,
            "RMSE": 10.678395276366356,
            "R2": 0.7544562538164442,
            "Memory in Mb": 0.0418310165405273,
            "Time in s": 1.031981
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 7.351838545672251,
            "RMSE": 11.801369148896674,
            "R2": 0.7361015298851068,
            "Memory in Mb": 0.0418310165405273,
            "Time in s": 1.114342
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 7.621792166351879,
            "RMSE": 12.282711040561283,
            "R2": 0.7524071035845484,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.198422
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 7.637256630205925,
            "RMSE": 12.295347873811286,
            "R2": 0.7848229800793282,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.284253
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 8.1943326666584,
            "RMSE": 13.18128308543095,
            "R2": 0.7797471460356308,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.3717719999999998
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 9.301321372784988,
            "RMSE": 15.883856969554804,
            "R2": 0.7097662534619076,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.4609289999999997
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 9.759535973032726,
            "RMSE": 16.540475274696632,
            "R2": 0.7306639846914664,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.5518979999999998
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 9.98108531256273,
            "RMSE": 16.6656027575944,
            "R2": 0.7551596457293974,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.6445489999999998
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 10.172493780682656,
            "RMSE": 16.824682995393008,
            "R2": 0.773160093080841,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.7389499999999998
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 11.068151856114426,
            "RMSE": 18.263714825485387,
            "R2": 0.7404354867888504,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.835003
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 11.603116520774073,
            "RMSE": 19.443156920913136,
            "R2": 0.7295745843003554,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 1.932986
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 12.00507936887919,
            "RMSE": 20.0961554988217,
            "R2": 0.744401153020958,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 2.032719
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 12.159003512064782,
            "RMSE": 20.104597547074984,
            "R2": 0.7614813985176707,
            "Memory in Mb": 0.0423574447631835,
            "Time in s": 2.134109
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 13.058561054914293,
            "RMSE": 21.64678300128301,
            "R2": 0.7429728504217219,
            "Memory in Mb": 0.0393133163452148,
            "Time in s": 2.2395339999999995
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 13.849374886718222,
            "RMSE": 23.13707582414104,
            "R2": 0.7243608784812086,
            "Memory in Mb": 0.039839744567871,
            "Time in s": 2.346639
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 14.418764158229274,
            "RMSE": 24.09396728520024,
            "R2": 0.7343803671174814,
            "Memory in Mb": 0.0408926010131835,
            "Time in s": 2.455353
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 14.611969435637262,
            "RMSE": 24.1872515908579,
            "R2": 0.7512659254336986,
            "Memory in Mb": 0.0414190292358398,
            "Time in s": 2.5657939999999995
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 15.14954210400284,
            "RMSE": 24.823452151261105,
            "R2": 0.7491462990276416,
            "Memory in Mb": 0.0429983139038085,
            "Time in s": 2.6778409999999995
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 16.266748325298664,
            "RMSE": 26.99226997645693,
            "R2": 0.7214095667925529,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 2.791571
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 17.063164501315207,
            "RMSE": 28.33702908143248,
            "R2": 0.7288823142196059,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 2.9070249999999995
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 17.41028324926407,
            "RMSE": 28.63458736095403,
            "R2": 0.7383292654808864,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.0241479999999994
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 17.881702409973563,
            "RMSE": 29.18189849457619,
            "R2": 0.7443486730566713,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.1430089999999997
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 18.783373559654446,
            "RMSE": 30.65392766804094,
            "R2": 0.7261055653266129,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.263499999999999
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 19.52135237811833,
            "RMSE": 31.66784012367412,
            "R2": 0.7241496029986892,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.3857279999999994
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 20.32410387080197,
            "RMSE": 32.88418602247989,
            "R2": 0.7325694870351915,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.509655999999999
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 20.50845806362208,
            "RMSE": 32.89095814819447,
            "R2": 0.7435070498169007,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.635277999999999
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 21.507291986413147,
            "RMSE": 34.52927015042095,
            "R2": 0.7260306568753008,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.762600999999999
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 22.222091157093345,
            "RMSE": 35.46412346985515,
            "R2": 0.7236334646353288,
            "Memory in Mb": 0.0435247421264648,
            "Time in s": 3.891587999999999
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "ChickWeights",
            "MAE": 23.084218600655667,
            "RMSE": 36.66377836765904,
            "R2": 0.7267728639741885,
            "Memory in Mb": 0.044051170349121,
            "Time in s": 4.022359999999999
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 4.834704431652337,
            "RMSE": 13.708514217962266,
            "R2": -439.7934984576362,
            "Memory in Mb": 0.0508193969726562,
            "Time in s": 0.006949
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 3.4692310697037447,
            "RMSE": 9.813795721313518,
            "R2": -37.72035957928713,
            "Memory in Mb": 0.0739822387695312,
            "Time in s": 0.020525
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.530247618203559,
            "RMSE": 8.024836796214231,
            "R2": -33.90460110966681,
            "Memory in Mb": 0.0866165161132812,
            "Time in s": 0.041034
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.1398752670733447,
            "RMSE": 6.982837000856316,
            "R2": -25.510487239912003,
            "Memory in Mb": 0.09661865234375,
            "Time in s": 0.06908
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.2521629689485394,
            "RMSE": 6.362737158647257,
            "R2": -12.810573390910957,
            "Memory in Mb": 0.1060943603515625,
            "Time in s": 0.105159
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.275331183116589,
            "RMSE": 5.895687482983747,
            "R2": -9.059182991303912,
            "Memory in Mb": 0.1103057861328125,
            "Time in s": 0.149228
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.181766409647037,
            "RMSE": 5.493495699082884,
            "R2": -8.025069637302263,
            "Memory in Mb": 0.1124114990234375,
            "Time in s": 0.201546
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.0641207293789914,
            "RMSE": 5.165105496730293,
            "R2": -6.03588310696345,
            "Memory in Mb": 0.1166229248046875,
            "Time in s": 0.262282
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.9901037542149176,
            "RMSE": 4.906162642056599,
            "R2": -4.575276834209563,
            "Memory in Mb": 0.1187286376953125,
            "Time in s": 0.331582
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.854788525917255,
            "RMSE": 4.661016718308231,
            "R2": -4.0470005140641305,
            "Memory in Mb": 0.015085220336914,
            "Time in s": 0.422383
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.777996659033335,
            "RMSE": 4.4592908674997,
            "R2": -3.98319384245183,
            "Memory in Mb": 0.0312490463256835,
            "Time in s": 0.517121
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.696058551537428,
            "RMSE": 4.277699003809556,
            "R2": -3.620107687238352,
            "Memory in Mb": 0.0370397567749023,
            "Time in s": 0.616341
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.6130985138696277,
            "RMSE": 4.114896288193841,
            "R2": -3.332738894340625,
            "Memory in Mb": 0.044569969177246,
            "Time in s": 0.720441
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.5797289220452373,
            "RMSE": 3.98595914915012,
            "R2": -3.256494063385272,
            "Memory in Mb": 0.0575590133666992,
            "Time in s": 0.829564
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.5530598651848762,
            "RMSE": 3.87273637004692,
            "R2": -2.951592153393709,
            "Memory in Mb": 0.0675611495971679,
            "Time in s": 0.944355
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.487708679701559,
            "RMSE": 3.753298690745279,
            "R2": -2.895390019001044,
            "Memory in Mb": 0.0754575729370117,
            "Time in s": 1.064913
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.447577018485449,
            "RMSE": 3.651821310152781,
            "R2": -2.8968902417113367,
            "Memory in Mb": 0.0807218551635742,
            "Time in s": 1.191641
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.4679964351503354,
            "RMSE": 3.577735862687295,
            "R2": -2.771095017816483,
            "Memory in Mb": 0.0886182785034179,
            "Time in s": 1.324785
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.433746711521204,
            "RMSE": 3.490600620499155,
            "R2": -2.7138197592485107,
            "Memory in Mb": 0.0938825607299804,
            "Time in s": 1.4646529999999998
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.394545215153479,
            "RMSE": 3.4083536810761967,
            "R2": -2.640941921411436,
            "Memory in Mb": 0.1012525558471679,
            "Time in s": 1.611633
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.3582303513295786,
            "RMSE": 3.3304244373469776,
            "R2": -2.5913988321456767,
            "Memory in Mb": 0.1054639816284179,
            "Time in s": 1.7657539999999998
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.3237600646089562,
            "RMSE": 3.2576165394889824,
            "R2": -2.3739144098898306,
            "Memory in Mb": 0.1112546920776367,
            "Time in s": 1.927203
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.313374021763953,
            "RMSE": 3.19664903268704,
            "R2": -2.080839603370824,
            "Memory in Mb": 0.1196775436401367,
            "Time in s": 2.096272
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.2871329178228548,
            "RMSE": 3.1331240379472574,
            "R2": -1.891520259695389,
            "Memory in Mb": 0.1275739669799804,
            "Time in s": 2.277254
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.257405891185914,
            "RMSE": 3.073015209583509,
            "R2": -1.7232796098685204,
            "Memory in Mb": 0.1323118209838867,
            "Time in s": 2.471873
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.236691492049667,
            "RMSE": 3.017934049641527,
            "R2": -1.6311150670478525,
            "Memory in Mb": 0.1375761032104492,
            "Time in s": 2.675336
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.2120036461347103,
            "RMSE": 2.9640451937301795,
            "R2": -1.528689807762199,
            "Memory in Mb": 0.1396818161010742,
            "Time in s": 2.8858550000000003
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1973910792850353,
            "RMSE": 2.9159627023633448,
            "R2": -1.5056283897938432,
            "Memory in Mb": 0.1444196701049804,
            "Time in s": 3.1010690000000003
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1729976236433703,
            "RMSE": 2.867868059269123,
            "R2": -1.4835996265310456,
            "Memory in Mb": 0.1470518112182617,
            "Time in s": 3.321073
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.164383909889498,
            "RMSE": 2.8255860627341494,
            "R2": -1.384236602114556,
            "Memory in Mb": 0.1414899826049804,
            "Time in s": 3.5505340000000003
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1607847453289375,
            "RMSE": 2.7880287925830083,
            "R2": -1.2858933574415188,
            "Memory in Mb": 0.1441221237182617,
            "Time in s": 3.784549
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1488689392891114,
            "RMSE": 2.748475985188827,
            "R2": -1.179970998158682,
            "Memory in Mb": 0.1462278366088867,
            "Time in s": 4.023051000000001
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1353328006378431,
            "RMSE": 2.711500109160092,
            "R2": -1.1064542348150137,
            "Memory in Mb": 0.0933332443237304,
            "Time in s": 4.270219000000001
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1237673891934872,
            "RMSE": 2.67586665558629,
            "R2": -1.083872122585975,
            "Memory in Mb": 0.1028089523315429,
            "Time in s": 4.520950000000001
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1197870211993892,
            "RMSE": 2.6450513004918434,
            "R2": -1.0896316212520398,
            "Memory in Mb": 0.1107053756713867,
            "Time in s": 4.77542
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0988128320741315,
            "RMSE": 2.6090976903580367,
            "R2": -1.077879402293885,
            "Memory in Mb": 0.1170225143432617,
            "Time in s": 5.033773
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0821696401958585,
            "RMSE": 2.5758102479785587,
            "R2": -1.0239793040320149,
            "Memory in Mb": 0.1207075119018554,
            "Time in s": 5.296116
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0646778366488154,
            "RMSE": 2.542912274197232,
            "R2": -0.9939800998628658,
            "Memory in Mb": 0.1238660812377929,
            "Time in s": 5.562507999999999
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0458773095514022,
            "RMSE": 2.5110610332394967,
            "R2": -0.953051985319172,
            "Memory in Mb": 0.1301832199096679,
            "Time in s": 5.833025999999999
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.037522387437363,
            "RMSE": 2.4829468635274075,
            "R2": -0.9268335078372076,
            "Memory in Mb": 0.1405134201049804,
            "Time in s": 6.107975999999999
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0344825476074344,
            "RMSE": 2.459713101244265,
            "R2": -0.9117084698305152,
            "Memory in Mb": 0.1468305587768554,
            "Time in s": 6.387556999999999
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0265033672562451,
            "RMSE": 2.433853565150633,
            "R2": -0.8891007921837151,
            "Memory in Mb": 0.1505155563354492,
            "Time in s": 6.671677999999999
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0098876748057108,
            "RMSE": 2.406249644034785,
            "R2": -0.8433117943327111,
            "Memory in Mb": 0.1520948410034179,
            "Time in s": 6.960477999999999
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9987418826957182,
            "RMSE": 2.3807044173500915,
            "R2": -0.795415858642577,
            "Memory in Mb": 0.1552534103393554,
            "Time in s": 7.253952999999999
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9899512872354768,
            "RMSE": 2.356297962435036,
            "R2": -0.7662040947107138,
            "Memory in Mb": 0.1573591232299804,
            "Time in s": 7.552186999999999
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9763510674237786,
            "RMSE": 2.3315103197053237,
            "R2": -0.7576521562914318,
            "Memory in Mb": 0.1254529953002929,
            "Time in s": 7.860606999999999
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9721072130212216,
            "RMSE": 2.310027291919755,
            "R2": -0.7400479483856388,
            "Memory in Mb": 0.1344251632690429,
            "Time in s": 8.173459999999999
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9655343485152448,
            "RMSE": 2.289186508543074,
            "R2": -0.7266590967915565,
            "Memory in Mb": 0.1402158737182617,
            "Time in s": 8.490537999999999
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9583856890611192,
            "RMSE": 2.2686834337047155,
            "R2": -0.7288044208040367,
            "Memory in Mb": 0.1444272994995117,
            "Time in s": 8.812014999999999
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Hoeffding Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9497447679766952,
            "RMSE": 2.248146643879841,
            "R2": -0.7262238291744263,
            "Memory in Mb": 0.1486387252807617,
            "Time in s": 9.137959
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 8.051220648038832,
            "RMSE": 17.336198122120386,
            "R2": -385.8701660091343,
            "Memory in Mb": 0.0232887268066406,
            "Time in s": 0.00403
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.498502947359929,
            "RMSE": 12.28528637536428,
            "R2": -158.84524831763767,
            "Memory in Mb": 0.0249290466308593,
            "Time in s": 0.011609
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 3.4668695042339137,
            "RMSE": 10.074636808082968,
            "R2": -69.49212762837747,
            "Memory in Mb": 0.0301933288574218,
            "Time in s": 0.022078
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 2.7637805804889557,
            "RMSE": 8.735764655686483,
            "R2": -59.08259408516962,
            "Memory in Mb": 0.0313072204589843,
            "Time in s": 0.035307
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 2.814517498310432,
            "RMSE": 8.074396776941786,
            "R2": -11.726997097138026,
            "Memory in Mb": 0.0381507873535156,
            "Time in s": 0.051286
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 3.396900059747575,
            "RMSE": 7.862006773633152,
            "R2": -4.201378762014764,
            "Memory in Mb": 0.0476264953613281,
            "Time in s": 0.070551
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 3.8844336568547537,
            "RMSE": 7.782255505653143,
            "R2": -2.415785129732385,
            "Memory in Mb": 0.0540046691894531,
            "Time in s": 0.093692
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.068768385552718,
            "RMSE": 7.555909217267645,
            "R2": -1.9194502155140076,
            "Memory in Mb": 0.0597953796386718,
            "Time in s": 0.121065
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.311602452908636,
            "RMSE": 7.487314706483316,
            "R2": -1.3976387620786477,
            "Memory in Mb": 0.0608482360839843,
            "Time in s": 0.152902
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.261918758035323,
            "RMSE": 7.240982145259267,
            "R2": -0.5659557565320237,
            "Memory in Mb": 0.0624275207519531,
            "Time in s": 0.189312
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.32509570871032,
            "RMSE": 7.149348278127394,
            "R2": -0.1757051422939808,
            "Memory in Mb": 0.0624275207519531,
            "Time in s": 0.229979
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.243770455182887,
            "RMSE": 6.949556168474376,
            "R2": 0.0920549285716371,
            "Memory in Mb": 0.0624275207519531,
            "Time in s": 0.275055
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.119311205048765,
            "RMSE": 6.740083059431663,
            "R2": 0.3082592266545521,
            "Memory in Mb": 0.0241641998291015,
            "Time in s": 0.330922
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.094718549433554,
            "RMSE": 6.618738421062464,
            "R2": 0.4330929316851147,
            "Memory in Mb": 0.034926414489746,
            "Time in s": 0.389383
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.353591485820727,
            "RMSE": 6.858418841195889,
            "R2": 0.5106778054828556,
            "Memory in Mb": 0.041365623474121,
            "Time in s": 0.450937
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.494676115333661,
            "RMSE": 6.99651956882687,
            "R2": 0.5894091082089881,
            "Memory in Mb": 0.0471563339233398,
            "Time in s": 0.515937
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.531460188122701,
            "RMSE": 6.982633238942946,
            "R2": 0.6651551017011323,
            "Memory in Mb": 0.052016258239746,
            "Time in s": 0.584675
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.550856564096301,
            "RMSE": 6.948954565412159,
            "R2": 0.736210476532317,
            "Memory in Mb": 0.0546483993530273,
            "Time in s": 0.6572239999999999
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 4.745146525796211,
            "RMSE": 7.286245359964537,
            "R2": 0.7609173164436883,
            "Memory in Mb": 0.0546483993530273,
            "Time in s": 0.733675
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 5.330595718754616,
            "RMSE": 8.515887777891804,
            "R2": 0.7140722769094752,
            "Memory in Mb": 0.0552968978881835,
            "Time in s": 0.814194
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 5.50563091305374,
            "RMSE": 8.701126762111178,
            "R2": 0.7446721431039482,
            "Memory in Mb": 0.0552968978881835,
            "Time in s": 0.898563
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 5.723610994733609,
            "RMSE": 9.068119167211083,
            "R2": 0.7768542529953268,
            "Memory in Mb": 0.0552968978881835,
            "Time in s": 0.986859
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 5.834317193911452,
            "RMSE": 9.203767847944404,
            "R2": 0.8003533769470821,
            "Memory in Mb": 0.0552968978881835,
            "Time in s": 1.07894
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 6.561326226922799,
            "RMSE": 10.595386608942691,
            "R2": 0.7582588922727441,
            "Memory in Mb": 0.0553770065307617,
            "Time in s": 1.17475
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 7.055343281410319,
            "RMSE": 11.793355798881397,
            "R2": 0.7364597921881992,
            "Memory in Mb": 0.0553770065307617,
            "Time in s": 1.274735
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 7.331998951413002,
            "RMSE": 12.245186296589464,
            "R2": 0.7539176280650666,
            "Memory in Mb": 0.0539121627807617,
            "Time in s": 1.383231
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 7.416966166983629,
            "RMSE": 12.289761227218738,
            "R2": 0.7850184759487971,
            "Memory in Mb": 0.0544385910034179,
            "Time in s": 1.495361
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 7.99448083149163,
            "RMSE": 13.217085318753208,
            "R2": 0.7785490451915651,
            "Memory in Mb": 0.0545606613159179,
            "Time in s": 1.6112419999999998
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 9.157233410060112,
            "RMSE": 16.13339057164046,
            "R2": 0.7005755447430102,
            "Memory in Mb": 0.0561399459838867,
            "Time in s": 1.73087
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 9.47509121278654,
            "RMSE": 16.446724789755304,
            "R2": 0.7337084949314072,
            "Memory in Mb": 0.0561399459838867,
            "Time in s": 1.854306
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 9.757592549477597,
            "RMSE": 16.701217161288277,
            "R2": 0.7541120796137563,
            "Memory in Mb": 0.0561399459838867,
            "Time in s": 1.981549
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 9.93501095513177,
            "RMSE": 16.87017564150386,
            "R2": 0.7719317193583981,
            "Memory in Mb": 0.0561399459838867,
            "Time in s": 2.112498
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 10.85670423687554,
            "RMSE": 18.405576814105093,
            "R2": 0.7363875320655082,
            "Memory in Mb": 0.0561399459838867,
            "Time in s": 2.247206
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 11.59956477803306,
            "RMSE": 20.214372545093333,
            "R2": 0.7076961913412723,
            "Memory in Mb": 0.0658864974975586,
            "Time in s": 2.386792
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 12.011712885443345,
            "RMSE": 20.838356414394227,
            "R2": 0.7251727140820715,
            "Memory in Mb": 0.0713338851928711,
            "Time in s": 2.531165
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 12.02179706392092,
            "RMSE": 20.699504894468426,
            "R2": 0.7471567277697432,
            "Memory in Mb": 0.0781774520874023,
            "Time in s": 2.680539
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 12.867904342374958,
            "RMSE": 22.04935022682606,
            "R2": 0.733324041761514,
            "Memory in Mb": 0.0825719833374023,
            "Time in s": 2.8351709999999994
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 13.7726214629037,
            "RMSE": 23.76360253855293,
            "R2": 0.7092307493255587,
            "Memory in Mb": 0.0846776962280273,
            "Time in s": 2.9951159999999994
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 14.320664029675132,
            "RMSE": 24.67720892632965,
            "R2": 0.7213650338700139,
            "Memory in Mb": 0.0656805038452148,
            "Time in s": 3.164622
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 14.560745017781516,
            "RMSE": 24.854467305977835,
            "R2": 0.7373537773889289,
            "Memory in Mb": 0.0706624984741211,
            "Time in s": 3.338776
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 15.05271815758178,
            "RMSE": 25.416929688531035,
            "R2": 0.7370081245929037,
            "Memory in Mb": 0.0787420272827148,
            "Time in s": 3.5178329999999995
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 16.182360709465044,
            "RMSE": 27.521690548068367,
            "R2": 0.7103739673524856,
            "Memory in Mb": 0.0857076644897461,
            "Time in s": 3.702085
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 17.028395162723214,
            "RMSE": 29.038217655150596,
            "R2": 0.7152989103492285,
            "Memory in Mb": 0.0888662338256836,
            "Time in s": 3.891670999999999
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 17.39410374569335,
            "RMSE": 29.368989764604034,
            "R2": 0.7247347991767862,
            "Memory in Mb": 0.0889272689819336,
            "Time in s": 4.084988999999999
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 17.903720470221085,
            "RMSE": 29.931789274576047,
            "R2": 0.7310408495158558,
            "Memory in Mb": 0.0889272689819336,
            "Time in s": 4.281388999999999
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 18.828904303353827,
            "RMSE": 31.360943457558232,
            "R2": 0.7133254165496098,
            "Memory in Mb": 0.0895147323608398,
            "Time in s": 4.480870999999999
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 19.65231385288099,
            "RMSE": 32.53535290181733,
            "R2": 0.7088292337107098,
            "Memory in Mb": 0.0743856430053711,
            "Time in s": 4.686204999999998
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 20.485248099981963,
            "RMSE": 33.800991401884744,
            "R2": 0.7174497851371298,
            "Memory in Mb": 0.0787191390991211,
            "Time in s": 4.894319999999999
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 20.62693587606907,
            "RMSE": 33.76714158926765,
            "R2": 0.7296595823775684,
            "Memory in Mb": 0.0872030258178711,
            "Time in s": 5.105511999999998
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 21.61100465238265,
            "RMSE": 35.363345192969206,
            "R2": 0.7126350131259431,
            "Memory in Mb": 0.0935201644897461,
            "Time in s": 5.319765999999999
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 22.391562087266266,
            "RMSE": 36.4058649659661,
            "R2": 0.708760885936744,
            "Memory in Mb": 0.0934362411499023,
            "Time in s": 5.537231999999999
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "ChickWeights",
            "MAE": 23.25574522992599,
            "RMSE": 37.57896806973795,
            "R2": 0.7129622004044582,
            "Memory in Mb": 0.0946111679077148,
            "Time in s": 5.757816999999998
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 4.828377634536296,
            "RMSE": 13.70786256219322,
            "R2": -439.7515918302183,
            "Memory in Mb": 0.0575942993164062,
            "Time in s": 0.005178
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 3.453811275213839,
            "RMSE": 9.811073218407971,
            "R2": -37.69887927291551,
            "Memory in Mb": 0.0808181762695312,
            "Time in s": 0.01451
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.5116544078850294,
            "RMSE": 8.021960641037959,
            "R2": -33.879585508404254,
            "Memory in Mb": 0.0934524536132812,
            "Time in s": 0.027873
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.1224425015381523,
            "RMSE": 6.9797990571526345,
            "R2": -25.487425023640156,
            "Memory in Mb": 0.103515625,
            "Time in s": 0.045557
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.246653919301699,
            "RMSE": 6.363694444016854,
            "R2": -12.814729355257526,
            "Memory in Mb": 0.1129913330078125,
            "Time in s": 0.06794
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.270681160376927,
            "RMSE": 5.896666779393501,
            "R2": -9.06252500695684,
            "Memory in Mb": 0.1172027587890625,
            "Time in s": 0.095003
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 2.1411489845018936,
            "RMSE": 5.486121567062232,
            "R2": -8.000856498367144,
            "Memory in Mb": 0.1193084716796875,
            "Time in s": 0.126859
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.9595309296437795,
            "RMSE": 5.145701533389061,
            "R2": -5.983118424699933,
            "Memory in Mb": 0.048110008239746,
            "Time in s": 0.170894
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.8606850760789413,
            "RMSE": 4.874784956472401,
            "R2": -4.504190782470528,
            "Memory in Mb": 0.0645513534545898,
            "Time in s": 0.218268
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.753768292507887,
            "RMSE": 4.635064394721464,
            "R2": -3.990954055000616,
            "Memory in Mb": 0.0751142501831054,
            "Time in s": 0.2693379999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.6442100676088158,
            "RMSE": 4.426753978888705,
            "R2": -3.910740120483753,
            "Memory in Mb": 0.0809926986694336,
            "Time in s": 0.324221
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.5586094458315778,
            "RMSE": 4.243291414416048,
            "R2": -3.546083102970604,
            "Memory in Mb": 0.0831594467163086,
            "Time in s": 0.383071
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.4757349309283123,
            "RMSE": 4.079934399827006,
            "R2": -3.259426129696055,
            "Memory in Mb": 0.0869779586791992,
            "Time in s": 0.445946
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.429182741517093,
            "RMSE": 3.94384178403937,
            "R2": -3.1670173911200505,
            "Memory in Mb": 0.0965147018432617,
            "Time in s": 0.513038
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.395554812880875,
            "RMSE": 3.827170050036498,
            "R2": -2.859150937529973,
            "Memory in Mb": 0.1050596237182617,
            "Time in s": 0.584571
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.342072644309252,
            "RMSE": 3.7085248950294263,
            "R2": -2.8030066952692625,
            "Memory in Mb": 0.1113767623901367,
            "Time in s": 0.660678
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.2981450416106572,
            "RMSE": 3.6023493777501,
            "R2": -2.7920215666096264,
            "Memory in Mb": 0.0969266891479492,
            "Time in s": 0.7468359999999999
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.3017629599133824,
            "RMSE": 3.52722030011446,
            "R2": -2.665355451896766,
            "Memory in Mb": 0.1048231124877929,
            "Time in s": 0.837109
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.2791887566109008,
            "RMSE": 3.4421979658375847,
            "R2": -2.6115379824259644,
            "Memory in Mb": 0.1101484298706054,
            "Time in s": 0.931726
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.2309239845123985,
            "RMSE": 3.35653802988408,
            "R2": -2.531080237482485,
            "Memory in Mb": 0.1175184249877929,
            "Time in s": 1.030965
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.204488166009232,
            "RMSE": 3.279580566778272,
            "R2": -2.4825797995498564,
            "Memory in Mb": 0.1217298507690429,
            "Time in s": 1.13497
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1805943216757937,
            "RMSE": 3.209931042788128,
            "R2": -2.2758615914195226,
            "Memory in Mb": 0.1275205612182617,
            "Time in s": 1.243696
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1747748413206256,
            "RMSE": 3.150463961675437,
            "R2": -1.9924589881120156,
            "Memory in Mb": 0.1354780197143554,
            "Time in s": 1.3572460000000002
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1643181646721343,
            "RMSE": 3.0907225956471227,
            "R2": -1.8137863387673288,
            "Memory in Mb": 0.1433744430541992,
            "Time in s": 1.47581
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1467427258000205,
            "RMSE": 3.033773569773335,
            "R2": -1.6541724792729693,
            "Memory in Mb": 0.1362333297729492,
            "Time in s": 1.6042770000000002
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1310531754619513,
            "RMSE": 2.979836071514613,
            "R2": -1.5651047078316291,
            "Memory in Mb": 0.1415586471557617,
            "Time in s": 1.7377410000000002
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1142715036195536,
            "RMSE": 2.927551584361061,
            "R2": -1.466806182052764,
            "Memory in Mb": 0.1436643600463867,
            "Time in s": 1.876231
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.1052485405576076,
            "RMSE": 2.88137538641146,
            "R2": -1.4465405352520455,
            "Memory in Mb": 0.1484022140502929,
            "Time in s": 2.0198690000000004
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0859142446379713,
            "RMSE": 2.834429565013283,
            "R2": -1.4260211929714153,
            "Memory in Mb": 0.1510343551635742,
            "Time in s": 2.168629
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0769717813954385,
            "RMSE": 2.7922355683541964,
            "R2": -1.3282862925750138,
            "Memory in Mb": 0.1547193527221679,
            "Time in s": 2.322692
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0766885404316004,
            "RMSE": 2.756385805344716,
            "R2": -1.234299900153052,
            "Memory in Mb": 0.1578779220581054,
            "Time in s": 2.481953
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.066276571170311,
            "RMSE": 2.7176435544384367,
            "R2": -1.1313354614936588,
            "Memory in Mb": 0.1599836349487304,
            "Time in s": 2.646434
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0564634149761172,
            "RMSE": 2.6824145051502803,
            "R2": -1.061505763110988,
            "Memory in Mb": 0.1636686325073242,
            "Time in s": 2.816279
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0488950225738152,
            "RMSE": 2.6482621618516,
            "R2": -1.0410990478472515,
            "Memory in Mb": 0.1663007736206054,
            "Time in s": 2.991546
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0494335446356584,
            "RMSE": 2.619695292588707,
            "R2": -1.0497603683353351,
            "Memory in Mb": 0.1547193527221679,
            "Time in s": 3.177748
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0311572549278785,
            "RMSE": 2.584165722213007,
            "R2": -1.038357615399126,
            "Memory in Mb": 0.1594572067260742,
            "Time in s": 3.369155
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 1.0166711191684197,
            "RMSE": 2.551525288520744,
            "R2": -0.9859947129346353,
            "Memory in Mb": 0.1632032394409179,
            "Time in s": 3.565871
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.998612246058934,
            "RMSE": 2.518502326974768,
            "R2": -0.9558825700512557,
            "Memory in Mb": 0.1647825241088867,
            "Time in s": 3.768021
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9842422617410423,
            "RMSE": 2.4876653972852822,
            "R2": -0.916828228451222,
            "Memory in Mb": 0.1695814132690429,
            "Time in s": 3.975687
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9822601758268574,
            "RMSE": 2.462050972175237,
            "R2": -0.8945384291924348,
            "Memory in Mb": 0.1616849899291992,
            "Time in s": 4.194112
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9867607749501652,
            "RMSE": 2.442599600947298,
            "R2": -0.8851995145588711,
            "Memory in Mb": 0.1643171310424804,
            "Time in s": 4.4181
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9793985197413392,
            "RMSE": 2.417271328475225,
            "R2": -0.8634469862274994,
            "Memory in Mb": 0.1680021286010742,
            "Time in s": 4.647504
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9647458553132984,
            "RMSE": 2.3903176435066817,
            "R2": -0.8189831286734526,
            "Memory in Mb": 0.1701078414916992,
            "Time in s": 4.882465
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9550000119490066,
            "RMSE": 2.3652388018081414,
            "R2": -0.7721647401587992,
            "Memory in Mb": 0.1727399826049804,
            "Time in s": 5.123038
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.945028697359752,
            "RMSE": 2.34076619049233,
            "R2": -0.7429966155689833,
            "Memory in Mb": 0.1115369796752929,
            "Time in s": 5.374164
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9340382087332012,
            "RMSE": 2.316653968016665,
            "R2": -0.7353240501222194,
            "Memory in Mb": 0.1163969039916992,
            "Time in s": 5.629799
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.93159447743873,
            "RMSE": 2.295899595899596,
            "R2": -0.7188294143518761,
            "Memory in Mb": 0.1223096847534179,
            "Time in s": 5.8899680000000005
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9266882702688716,
            "RMSE": 2.2758824318695603,
            "R2": -0.7066477496763941,
            "Memory in Mb": 0.1296796798706054,
            "Time in s": 6.154803
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.9199947893356224,
            "RMSE": 2.255690063945526,
            "R2": -0.7090584581073034,
            "Memory in Mb": 0.1349439620971679,
            "Time in s": 6.424549
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Hoeffding Adaptive Tree",
            "dataset": "TrumpApproval",
            "MAE": 0.910675347240908,
            "RMSE": 2.2342958873570486,
            "R2": -0.7050189374098543,
            "Memory in Mb": 0.1382246017456054,
            "Time in s": 6.699174
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 41.63636363636363,
            "RMSE": 41.64569169030137,
            "R2": -2231.5319148936137,
            "Memory in Mb": 0.0096149444580078,
            "Time in s": 0.001833
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 41.31818181818181,
            "RMSE": 41.32960638133835,
            "R2": -1808.0547045951903,
            "Memory in Mb": 0.0126094818115234,
            "Time in s": 0.00539
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 41.12121212121212,
            "RMSE": 41.13871582091424,
            "R2": -1174.393494897962,
            "Memory in Mb": 0.015787124633789,
            "Time in s": 0.009921
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 41.159090909090914,
            "RMSE": 41.17451771534076,
            "R2": -1333.7620984139928,
            "Memory in Mb": 0.0188732147216796,
            "Time in s": 0.015497
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 41.5090909090909,
            "RMSE": 41.57075020645253,
            "R2": -336.3506066081568,
            "Memory in Mb": 0.0218257904052734,
            "Time in s": 0.022338
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 42.681818181818166,
            "RMSE": 42.82080349691271,
            "R2": -153.29834830483878,
            "Memory in Mb": 0.0246181488037109,
            "Time in s": 0.030239
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 43.50649350649351,
            "RMSE": 43.70978671356627,
            "R2": -106.75487995129542,
            "Memory in Mb": 0.0275020599365234,
            "Time in s": 0.039152
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 44.21590909090909,
            "RMSE": 44.43649707984724,
            "R2": -99.97346126163,
            "Memory in Mb": 0.0300197601318359,
            "Time in s": 0.049123
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 45.05050505050505,
            "RMSE": 45.309262771858165,
            "R2": -86.8022342468144,
            "Memory in Mb": 0.0329036712646484,
            "Time in s": 0.060256
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 46.16363636363636,
            "RMSE": 46.52487115902242,
            "R2": -63.64797006437341,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.074892
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 47.21487603305785,
            "RMSE": 47.67304278378361,
            "R2": -51.27707184490422,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.095588
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 48.29545454545455,
            "RMSE": 48.843054157105485,
            "R2": -43.84882422437649,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.122121
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 49.44055944055945,
            "RMSE": 50.100318941519305,
            "R2": -37.220279564063546,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.154488
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 50.532467532467535,
            "RMSE": 51.29137544271156,
            "R2": -33.04474826644667,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.192654
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 51.690909090909095,
            "RMSE": 52.61253451297311,
            "R2": -27.795548438273773,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.236647
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 53.00568181818182,
            "RMSE": 54.11860921749895,
            "R2": -23.566226925646237,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.286373
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 54.41176470588235,
            "RMSE": 55.733754017636336,
            "R2": -20.33250305682894,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.341821
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 56.02525252525252,
            "RMSE": 57.635786091488654,
            "R2": -17.146924852486976,
            "Memory in Mb": 0.2696781158447265,
            "Time in s": 0.403009
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 55.16354936929098,
            "RMSE": 57.0482200725598,
            "R2": -13.656313160472004,
            "Memory in Mb": 0.6838865280151367,
            "Time in s": 0.4890500000000001
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 53.62203856749311,
            "RMSE": 56.03531795068661,
            "R2": -11.37998411824978,
            "Memory in Mb": 0.6869077682495117,
            "Time in s": 0.5845720000000001
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.77279286370195,
            "RMSE": 55.29408706815337,
            "R2": -9.311090357596036,
            "Memory in Mb": 0.6899290084838867,
            "Time in s": 0.6897040000000001
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.49661908339594,
            "RMSE": 55.0071045368674,
            "R2": -7.210918602421254,
            "Memory in Mb": 0.6929502487182617,
            "Time in s": 0.8041680000000001
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.25631812193077,
            "RMSE": 54.71344660515688,
            "R2": -6.055353919833875,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 0.92814
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 51.62511478420569,
            "RMSE": 54.312843786153664,
            "R2": -5.352168023774992,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.061635
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 51.4425344352617,
            "RMSE": 54.29364548356293,
            "R2": -4.585603291722447,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.204612
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 51.75651621106165,
            "RMSE": 54.635705044608144,
            "R2": -3.8989478253777694,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.357118
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.373839404142416,
            "RMSE": 55.25476711535166,
            "R2": -3.3456400671942,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.518976
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.87239275875638,
            "RMSE": 55.86677247417265,
            "R2": -2.9565197175813718,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.690095
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 52.69554478958866,
            "RMSE": 56.2770501442128,
            "R2": -2.6433309475704183,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 1.870449
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 53.85316804407712,
            "RMSE": 57.75044402630399,
            "R2": -2.2832890424968197,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 2.06005
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 54.90678041411178,
            "RMSE": 59.01114057562677,
            "R2": -2.0697921090482247,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 2.258925
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 56.00533746556472,
            "RMSE": 60.30224520856101,
            "R2": -1.9140207825503284,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 2.467073
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 55.99599298772852,
            "RMSE": 60.54917173074773,
            "R2": -1.852879941931207,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 2.684461
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 56.87222492302705,
            "RMSE": 61.81275171085535,
            "R2": -1.7331917323651345,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 2.911073
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 58.41786698150333,
            "RMSE": 63.95254893573906,
            "R2": -1.588502821427925,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 3.146928
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 59.7033976124885,
            "RMSE": 65.46926983257002,
            "R2": -1.5293357430909813,
            "Memory in Mb": 0.6947126388549805,
            "Time in s": 3.392032
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 60.057805647389294,
            "RMSE": 66.17359973042984,
            "R2": -1.4019380007417157,
            "Memory in Mb": 1.1097631454467771,
            "Time in s": 3.672033
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 59.7070864579051,
            "RMSE": 66.11592086962122,
            "R2": -1.2507954049688483,
            "Memory in Mb": 1.1127843856811523,
            "Time in s": 3.965768
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 60.122823673891816,
            "RMSE": 66.73609937588846,
            "R2": -1.0378169857688957,
            "Memory in Mb": 1.1158056259155271,
            "Time in s": 4.272702
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 60.39504675635191,
            "RMSE": 66.96100690444877,
            "R2": -0.906365593827489,
            "Memory in Mb": 1.1188268661499023,
            "Time in s": 4.593074
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 60.27126048587789,
            "RMSE": 66.93502892662679,
            "R2": -0.8239085862185902,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 4.926735
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 60.340686610373176,
            "RMSE": 67.43825007380137,
            "R2": -0.7390015352251049,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 5.273856
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 61.40703262301831,
            "RMSE": 69.11306667757516,
            "R2": -0.6127592621572406,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 5.634397
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 61.95796621360106,
            "RMSE": 69.71422620021941,
            "R2": -0.5510154280248158,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 6.008344
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 62.59018166487368,
            "RMSE": 70.55352405729404,
            "R2": -0.4943708535906215,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 6.395653
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 62.49664579133251,
            "RMSE": 70.88193125644693,
            "R2": -0.4644752452013045,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 6.796304
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 63.25224079915844,
            "RMSE": 71.92080214464903,
            "R2": -0.4228062717918979,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 7.21023
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 64.80783657170488,
            "RMSE": 74.3681944005728,
            "R2": -0.367764222300833,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 7.637592
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 65.59959781369417,
            "RMSE": 75.30113885843834,
            "R2": -0.3443906138479853,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 8.078512
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 65.79684627343133,
            "RMSE": 76.01328745307667,
            "R2": -0.3277190973108916,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 8.532886
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 66.6512855136148,
            "RMSE": 77.20436469287773,
            "R2": -0.3097569166669509,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 9.000807
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "ChickWeights",
            "MAE": 68.11975592628174,
            "RMSE": 79.56492566870935,
            "R2": -0.2867456678376987,
            "Memory in Mb": 1.120589256286621,
            "Time in s": 9.482145
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 43.8732195,
            "RMSE": 43.87807788634269,
            "R2": -4514.954899312423,
            "Memory in Mb": 0.0199413299560546,
            "Time in s": 0.002755
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 42.4932955,
            "RMSE": 42.52255283421693,
            "R2": -725.9491167623446,
            "Memory in Mb": 0.0317363739013671,
            "Time in s": 0.008058
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 42.2167785,
            "RMSE": 42.2386240157387,
            "R2": -966.0073736019044,
            "Memory in Mb": 0.0438976287841796,
            "Time in s": 0.015549
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 41.975705625,
            "RMSE": 41.99760868559829,
            "R2": -957.9655948743646,
            "Memory in Mb": 0.0562419891357421,
            "Time in s": 0.025294
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 41.37550450000001,
            "RMSE": 41.410913785433536,
            "R2": -583.9966399141301,
            "Memory in Mb": 0.5381031036376953,
            "Time in s": 0.041246
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 40.936110000000006,
            "RMSE": 40.97829382197767,
            "R2": -484.9611418859003,
            "Memory in Mb": 0.5386066436767578,
            "Time in s": 0.070023
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 40.6885472857143,
            "RMSE": 40.72961738075088,
            "R2": -495.1050461477588,
            "Memory in Mb": 0.5391101837158203,
            "Time in s": 0.110787
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 40.35105437500001,
            "RMSE": 40.39801158334292,
            "R2": -429.4078677932073,
            "Memory in Mb": 0.5393619537353516,
            "Time in s": 0.163463
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 40.00981655555555,
            "RMSE": 40.06373388340122,
            "R2": -370.7794659133543,
            "Memory in Mb": 0.5396137237548828,
            "Time in s": 0.227995
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 39.80633095,
            "RMSE": 39.860362966711,
            "R2": -368.1089073295326,
            "Memory in Mb": 0.5077581405639648,
            "Time in s": 0.320041
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 36.497516001377406,
            "RMSE": 38.01945344470104,
            "R2": -361.2329206514933,
            "Memory in Mb": 1.3602590560913086,
            "Time in s": 0.441408
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 33.64243104419191,
            "RMSE": 36.40668421494773,
            "R2": -333.65237138497804,
            "Memory in Mb": 1.360762596130371,
            "Time in s": 0.581306
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 31.222114965034955,
            "RMSE": 34.98371838354962,
            "R2": -312.16748668977897,
            "Memory in Mb": 1.3610143661499023,
            "Time in s": 0.739627
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 29.18205946861472,
            "RMSE": 33.71869814960704,
            "R2": -303.5986275675674,
            "Memory in Mb": 1.361769676208496,
            "Time in s": 0.915776
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 27.34275770505051,
            "RMSE": 32.57805191350732,
            "R2": -278.63174197976707,
            "Memory in Mb": 1.3620214462280271,
            "Time in s": 1.109879
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 25.81388747443183,
            "RMSE": 31.5521424826706,
            "R2": -274.2849072221064,
            "Memory in Mb": 1.3630285263061523,
            "Time in s": 1.321838
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 24.51835124153299,
            "RMSE": 30.62414457186519,
            "R2": -273.0482727941538,
            "Memory in Mb": 1.3640356063842771,
            "Time in s": 1.551694
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 23.451930423400693,
            "RMSE": 29.78792492645533,
            "R2": -260.4155562259403,
            "Memory in Mb": 1.3660497665405271,
            "Time in s": 1.799643
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 22.46844053349284,
            "RMSE": 29.014219480552867,
            "R2": -255.5915105297988,
            "Memory in Mb": 1.3665533065795898,
            "Time in s": 2.065559
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 21.59490700757577,
            "RMSE": 28.301677882839343,
            "R2": -250.0434007116766,
            "Memory in Mb": 0.510127067565918,
            "Time in s": 2.355987
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 20.62268781294523,
            "RMSE": 27.62086591367872,
            "R2": -246.0239415518119,
            "Memory in Mb": 1.3623762130737305,
            "Time in s": 2.674434
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 19.786863931462925,
            "RMSE": 26.990398924900397,
            "R2": -230.60756767519212,
            "Memory in Mb": 1.3643903732299805,
            "Time in s": 3.010878
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 19.05732899619648,
            "RMSE": 26.404670160589287,
            "R2": -209.2038511633616,
            "Memory in Mb": 1.3666563034057615,
            "Time in s": 3.365293
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 18.376512097202227,
            "RMSE": 25.854792215140314,
            "R2": -195.90337768575387,
            "Memory in Mb": 1.3701810836791992,
            "Time in s": 3.737716
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 17.755044410127518,
            "RMSE": 25.338820973360427,
            "R2": -184.1550753065148,
            "Memory in Mb": 1.3716917037963867,
            "Time in s": 4.128280999999999
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 17.16611419898163,
            "RMSE": 24.851444862058347,
            "R2": -177.4118263333629,
            "Memory in Mb": 1.3737058639526367,
            "Time in s": 4.537221
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 16.628565596068775,
            "RMSE": 24.392285078947275,
            "R2": -170.25012213753183,
            "Memory in Mb": 1.3747129440307615,
            "Time in s": 4.964375
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 16.091244232649693,
            "RMSE": 23.955027361350904,
            "R2": -168.10096043791202,
            "Memory in Mb": 1.3752164840698242,
            "Time in s": 5.410107999999999
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 15.590768135673304,
            "RMSE": 23.54051091957351,
            "R2": -166.33817208986073,
            "Memory in Mb": 1.3764753341674805,
            "Time in s": 5.874175999999999
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 15.168708628495342,
            "RMSE": 23.15108754841241,
            "R2": -159.05714501634571,
            "Memory in Mb": 0.5124959945678711,
            "Time in s": 6.365194
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 14.742446374247312,
            "RMSE": 22.77953961802373,
            "R2": -151.59887848495535,
            "Memory in Mb": 3.064208030700684,
            "Time in s": 6.921285
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 14.319364852585176,
            "RMSE": 22.42187566882095,
            "R2": -144.08105420081068,
            "Memory in Mb": 3.0679845809936523,
            "Time in s": 7.51197
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 13.916412195872256,
            "RMSE": 22.080274918425697,
            "R2": -138.68241285181185,
            "Memory in Mb": 3.0712575912475586,
            "Time in s": 8.136981
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 13.515604789075644,
            "RMSE": 21.753254558457893,
            "R2": -136.71797028279042,
            "Memory in Mb": 3.074782371520996,
            "Time in s": 8.796442
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 13.16391092204058,
            "RMSE": 21.44141764506316,
            "R2": -136.3120101768532,
            "Memory in Mb": 3.0773000717163086,
            "Time in s": 9.490636
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 12.828283113852926,
            "RMSE": 21.142484202016185,
            "R2": -135.44313416922282,
            "Memory in Mb": 3.078558921813965,
            "Time in s": 10.219341
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 12.50446646701278,
            "RMSE": 20.855361315179096,
            "R2": -131.6825380828392,
            "Memory in Mb": 3.0800695419311523,
            "Time in s": 10.982324
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 12.187542748969031,
            "RMSE": 20.57929219886472,
            "R2": -129.592708960364,
            "Memory in Mb": 3.0813283920288086,
            "Time in s": 11.779656
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 11.899403743710543,
            "RMSE": 20.31464229706916,
            "R2": -126.82553676745258,
            "Memory in Mb": 3.08359432220459,
            "Time in s": 12.611571
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 11.634366305883283,
            "RMSE": 20.06137952581079,
            "R2": -124.7856004590591,
            "Memory in Mb": 3.084601402282715,
            "Time in s": 13.493909000000002
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 11.363415331478278,
            "RMSE": 19.815492221289517,
            "R2": -123.0687724200615,
            "Memory in Mb": 3.08560848236084,
            "Time in s": 14.412321000000002
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 11.106640469158773,
            "RMSE": 19.57848368678801,
            "R2": -121.2430978899656,
            "Memory in Mb": 3.086615562438965,
            "Time in s": 15.363464000000002
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 10.873909665943762,
            "RMSE": 19.35022618912736,
            "R2": -118.20364312373844,
            "Memory in Mb": 3.087119102478028,
            "Time in s": 16.347229000000002
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 10.65545006969969,
            "RMSE": 19.130035299019603,
            "R2": -114.92727947355436,
            "Memory in Mb": 3.0873708724975586,
            "Time in s": 17.36361
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 10.439309697188907,
            "RMSE": 18.916827199314994,
            "R2": -112.83532852765144,
            "Memory in Mb": 3.08762264251709,
            "Time in s": 18.412326
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 10.21789524284777,
            "RMSE": 18.710158789526105,
            "R2": -112.19133803320568,
            "Memory in Mb": 3.087874412536621,
            "Time in s": 19.493438
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 10.012578535125469,
            "RMSE": 18.510293787577226,
            "R2": -110.72583714230213,
            "Memory in Mb": 3.077906608581543,
            "Time in s": 20.736809
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 9.811853150109153,
            "RMSE": 18.316579311485903,
            "R2": -109.54344305213982,
            "Memory in Mb": 3.0804243087768555,
            "Time in s": 22.013587
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 9.61909067795052,
            "RMSE": 18.12881604876013,
            "R2": -109.39183420714345,
            "Memory in Mb": 3.080927848815918,
            "Time in s": 23.322572
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Stochastic Gradient Tree",
            "dataset": "TrumpApproval",
            "MAE": 9.438738635632271,
            "RMSE": 17.946847607318464,
            "R2": -109.00797869183796,
            "Memory in Mb": 3.082438468933105,
            "Time in s": 24.663779
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 7.837563210503649,
            "RMSE": 16.830121687224917,
            "R2": -363.61289911513376,
            "Memory in Mb": 0.1506233215332031,
            "Time in s": 0.018991
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 4.3557641651310055,
            "RMSE": 11.925612892987612,
            "R2": -149.62275175212707,
            "Memory in Mb": 0.1761512756347656,
            "Time in s": 0.051966
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 3.371112580593177,
            "RMSE": 9.780386843070694,
            "R2": -65.43453306461763,
            "Memory in Mb": 0.2142868041992187,
            "Time in s": 0.1028409999999999
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 2.695097509519297,
            "RMSE": 8.482165721989492,
            "R2": -55.64483692929184,
            "Memory in Mb": 0.2312774658203125,
            "Time in s": 0.1714339999999999
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 2.750371500828058,
            "RMSE": 7.825470627419848,
            "R2": -10.954370249441634,
            "Memory in Mb": 0.2869682312011719,
            "Time in s": 0.2559499999999999
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 2.874973614360605,
            "RMSE": 7.312672972792191,
            "R2": -3.4999113348114523,
            "Memory in Mb": 0.3332901000976562,
            "Time in s": 0.3603679999999999
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 3.049190601733834,
            "RMSE": 7.064366487423796,
            "R2": -1.814660484448317,
            "Memory in Mb": 0.3119354248046875,
            "Time in s": 0.4921819999999999
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 2.9760015514160614,
            "RMSE": 6.690266116634344,
            "R2": -1.2888345310585096,
            "Memory in Mb": 0.3463325500488281,
            "Time in s": 0.6436869999999999
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 3.4458208345296213,
            "RMSE": 6.801756467406213,
            "R2": -0.9786716534372656,
            "Memory in Mb": 0.3914375305175781,
            "Time in s": 0.8148389999999999
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 3.8036130411377513,
            "RMSE": 6.901055458118455,
            "R2": -0.4223797783359673,
            "Memory in Mb": 0.4219093322753906,
            "Time in s": 1.008913
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 4.044286594485068,
            "RMSE": 6.961321070951229,
            "R2": -0.1146764842737158,
            "Memory in Mb": 0.4422340393066406,
            "Time in s": 1.227422
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 4.278051046290026,
            "RMSE": 6.992189163715883,
            "R2": 0.0808809347253165,
            "Memory in Mb": 0.4695549011230469,
            "Time in s": 1.467051
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 4.514698307868387,
            "RMSE": 7.09845673012605,
            "R2": 0.232743181062298,
            "Memory in Mb": 0.5039863586425781,
            "Time in s": 1.72858
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 4.711682816733759,
            "RMSE": 7.225211881769595,
            "R2": 0.3244420464758215,
            "Memory in Mb": 0.5465545654296875,
            "Time in s": 2.00923
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 5.098965674365188,
            "RMSE": 7.74448667501397,
            "R2": 0.3760752970367085,
            "Memory in Mb": 0.5543212890625,
            "Time in s": 2.317031
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 5.613573109580669,
            "RMSE": 8.405070008975855,
            "R2": 0.4074460804745814,
            "Memory in Mb": 0.5778732299804688,
            "Time in s": 2.650775
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 6.0300184245211925,
            "RMSE": 8.816070592615688,
            "R2": 0.4662285490406689,
            "Memory in Mb": 0.597381591796875,
            "Time in s": 3.008386
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 6.135166503700917,
            "RMSE": 8.873071763991604,
            "R2": 0.5699028278126741,
            "Memory in Mb": 0.6156463623046875,
            "Time in s": 3.389767
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 6.663870316688535,
            "RMSE": 9.680163486851024,
            "R2": 0.5780063435312484,
            "Memory in Mb": 0.6372909545898438,
            "Time in s": 3.797698
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 7.114976257039628,
            "RMSE": 10.70304519196575,
            "R2": 0.548340525531499,
            "Memory in Mb": 0.6516532897949219,
            "Time in s": 4.233731
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 7.558935022860611,
            "RMSE": 11.205896813348822,
            "R2": 0.5765126454701623,
            "Memory in Mb": 0.6456108093261719,
            "Time in s": 4.696369
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 7.8784966144348445,
            "RMSE": 11.546829616877767,
            "R2": 0.6381907286214681,
            "Memory in Mb": 0.6543197631835938,
            "Time in s": 5.184542
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 8.045465222989945,
            "RMSE": 11.7730800696534,
            "R2": 0.6733287963504477,
            "Memory in Mb": 0.6542396545410156,
            "Time in s": 5.698149999999999
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 8.55861765945315,
            "RMSE": 12.698578392308455,
            "R2": 0.6527621165047097,
            "Memory in Mb": 0.7007179260253906,
            "Time in s": 6.239901999999999
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 9.012932654808608,
            "RMSE": 13.883768164483952,
            "R2": 0.6347528903285174,
            "Memory in Mb": 0.7182159423828125,
            "Time in s": 6.810226999999999
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 9.46045520422096,
            "RMSE": 14.421722772543973,
            "R2": 0.6586625054492083,
            "Memory in Mb": 0.7397651672363281,
            "Time in s": 7.406784999999999
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 9.467084537445258,
            "RMSE": 14.393153360282469,
            "R2": 0.7051330126585751,
            "Memory in Mb": 0.6962127685546875,
            "Time in s": 8.032812
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 9.993822911601686,
            "RMSE": 15.306673373378164,
            "R2": 0.7029922374440833,
            "Memory in Mb": 0.712249755859375,
            "Time in s": 8.684709
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 10.906399564516825,
            "RMSE": 17.709412566907307,
            "R2": 0.6392184800849823,
            "Memory in Mb": 0.7230567932128906,
            "Time in s": 9.367603
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 11.354718196032138,
            "RMSE": 18.25739128586918,
            "R2": 0.6718473555535345,
            "Memory in Mb": 0.748199462890625,
            "Time in s": 10.07931
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 11.709200775641314,
            "RMSE": 18.709755653596343,
            "R2": 0.691413317744465,
            "Memory in Mb": 0.7508468627929688,
            "Time in s": 10.818764
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 12.007404346564588,
            "RMSE": 19.02446579939404,
            "R2": 0.7099648583835785,
            "Memory in Mb": 0.7794418334960938,
            "Time in s": 11.583692
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 12.612646669962947,
            "RMSE": 20.078004824306745,
            "R2": 0.6863045708062432,
            "Memory in Mb": 0.8219375610351562,
            "Time in s": 12.374611
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 13.305874945245664,
            "RMSE": 21.69198202373745,
            "R2": 0.6634013148524545,
            "Memory in Mb": 0.8368568420410156,
            "Time in s": 13.19172
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 13.874152914620147,
            "RMSE": 22.398641632517744,
            "R2": 0.6824761966895349,
            "Memory in Mb": 0.8399162292480469,
            "Time in s": 14.039444
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 14.02164789427361,
            "RMSE": 22.45496751107478,
            "R2": 0.7024524705388633,
            "Memory in Mb": 0.8451423645019531,
            "Time in s": 14.916422
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 14.881080524519056,
            "RMSE": 23.990711305579165,
            "R2": 0.684297135752792,
            "Memory in Mb": 0.844085693359375,
            "Time in s": 15.821424
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 15.672731015633325,
            "RMSE": 25.84901428202966,
            "R2": 0.6559576619146927,
            "Memory in Mb": 0.8621559143066406,
            "Time in s": 16.75642
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 16.52730145447373,
            "RMSE": 27.03527355015745,
            "R2": 0.6655701177301542,
            "Memory in Mb": 0.8826904296875,
            "Time in s": 17.718062999999997
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 16.835543678126854,
            "RMSE": 27.29532071757395,
            "R2": 0.6832339396752392,
            "Memory in Mb": 0.8854255676269531,
            "Time in s": 18.709096
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 17.2847401584601,
            "RMSE": 27.83347178305896,
            "R2": 0.6846223453976918,
            "Memory in Mb": 0.9156723022460938,
            "Time in s": 19.725565
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 18.263556988874104,
            "RMSE": 29.983264015814683,
            "R2": 0.6562480279042127,
            "Memory in Mb": 0.9476966857910156,
            "Time in s": 20.769031
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 19.168820167599023,
            "RMSE": 31.233753579350584,
            "R2": 0.6706197338145063,
            "Memory in Mb": 0.9631462097167968,
            "Time in s": 21.841163
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 19.66691155441429,
            "RMSE": 31.66292403296529,
            "R2": 0.6800549958221269,
            "Memory in Mb": 0.9797592163085938,
            "Time in s": 22.942597
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 20.1980005296915,
            "RMSE": 32.326142080110245,
            "R2": 0.6862897411402615,
            "Memory in Mb": 1.003559112548828,
            "Time in s": 24.073219
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 21.038101965066165,
            "RMSE": 33.861783151779306,
            "R2": 0.6657814123530009,
            "Memory in Mb": 1.0402488708496094,
            "Time in s": 25.232436
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 21.79336863548733,
            "RMSE": 34.905834748448235,
            "R2": 0.6648549707242759,
            "Memory in Mb": 1.059162139892578,
            "Time in s": 26.421057
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 22.71415913579816,
            "RMSE": 36.0778798798642,
            "R2": 0.6781016272298894,
            "Memory in Mb": 1.080280303955078,
            "Time in s": 27.640294
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 22.973012146363907,
            "RMSE": 36.13494365478664,
            "R2": 0.690416970144236,
            "Memory in Mb": 1.1105842590332031,
            "Time in s": 28.88878
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 23.822482702164027,
            "RMSE": 37.524990725820025,
            "R2": 0.6764299185798421,
            "Memory in Mb": 1.15643310546875,
            "Time in s": 30.16877
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 24.754282528765707,
            "RMSE": 38.80763200620001,
            "R2": 0.669066082535116,
            "Memory in Mb": 1.1719589233398438,
            "Time in s": 31.481567
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "ChickWeights",
            "MAE": 25.964764492717645,
            "RMSE": 40.6034258569803,
            "R2": 0.6648997528039327,
            "Memory in Mb": 1.186126708984375,
            "Time in s": 32.828648
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 4.656631863584941,
            "RMSE": 13.301513571178564,
            "R2": -414.0080590272913,
            "Memory in Mb": 0.20159912109375,
            "Time in s": 0.060655
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 3.3092233454389866,
            "RMSE": 9.514642226769206,
            "R2": -35.395716979334736,
            "Memory in Mb": 0.2895278930664062,
            "Time in s": 0.186458
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 2.370245548222252,
            "RMSE": 7.779742234417967,
            "R2": -31.80504797847069,
            "Memory in Mb": 0.3228263854980469,
            "Time in s": 0.354007
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 2.0011825545667588,
            "RMSE": 6.767036502792006,
            "R2": -23.897224712465302,
            "Memory in Mb": 0.3692893981933594,
            "Time in s": 0.55542
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 2.056871489932448,
            "RMSE": 6.139015712379544,
            "R2": -11.856454989718417,
            "Memory in Mb": 0.4076881408691406,
            "Time in s": 0.79515
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 2.003092266983848,
            "RMSE": 5.651046465030358,
            "R2": -8.241693395555247,
            "Memory in Mb": 0.4241790771484375,
            "Time in s": 1.072178
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.8854667406427696,
            "RMSE": 5.2532308662388045,
            "R2": -7.252888139218157,
            "Memory in Mb": 0.4439773559570312,
            "Time in s": 1.385482
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.9340845560700957,
            "RMSE": 4.984838031470717,
            "R2": -5.553334350331147,
            "Memory in Mb": 0.4557876586914062,
            "Time in s": 1.738613
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.9596878280460808,
            "RMSE": 4.757627458420989,
            "R2": -4.242801539132487,
            "Memory in Mb": 0.4726028442382812,
            "Time in s": 2.128929
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.9000266951648128,
            "RMSE": 4.53846274922039,
            "R2": -3.785084131964374,
            "Memory in Mb": 0.5018348693847656,
            "Time in s": 2.555084
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.7756062902244436,
            "RMSE": 4.331882031903988,
            "R2": -3.702506681895046,
            "Memory in Mb": 0.5390548706054688,
            "Time in s": 3.014926
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.722064335127714,
            "RMSE": 4.161337926832492,
            "R2": -3.3721758647478204,
            "Memory in Mb": 0.5583267211914062,
            "Time in s": 3.510014
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.668741133448935,
            "RMSE": 4.009095884933904,
            "R2": -3.112800247055813,
            "Memory in Mb": 0.5867843627929688,
            "Time in s": 4.039729
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.596023168515899,
            "RMSE": 3.86837254754146,
            "R2": -3.0090634555073343,
            "Memory in Mb": 0.6034698486328125,
            "Time in s": 4.6068750000000005
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.5862781822088614,
            "RMSE": 3.757725401796155,
            "R2": -2.72037165832895,
            "Memory in Mb": 0.6344451904296875,
            "Time in s": 5.213001
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.5269819355711358,
            "RMSE": 3.644015209511257,
            "R2": -2.67185104068617,
            "Memory in Mb": 0.6524238586425781,
            "Time in s": 5.854158
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.4570659608871932,
            "RMSE": 3.537119081966105,
            "R2": -2.6559352799702967,
            "Memory in Mb": 0.6771697998046875,
            "Time in s": 6.534176
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.4064005847783465,
            "RMSE": 3.441784227878547,
            "R2": -2.4899419787597266,
            "Memory in Mb": 0.7120590209960938,
            "Time in s": 7.253771
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.353481677960258,
            "RMSE": 3.352627624678765,
            "R2": -2.426029812278527,
            "Memory in Mb": 0.7612266540527344,
            "Time in s": 8.012458
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.3254238940946812,
            "RMSE": 3.27422063813923,
            "R2": -2.360008106665105,
            "Memory in Mb": 0.7831077575683594,
            "Time in s": 8.809453000000001
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.2822507927277378,
            "RMSE": 3.197239276537114,
            "R2": -2.309899038967682,
            "Memory in Mb": 0.8153495788574219,
            "Time in s": 9.645719
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.2469389910195894,
            "RMSE": 3.127027882921648,
            "R2": -2.108834809107039,
            "Memory in Mb": 0.8549957275390625,
            "Time in s": 10.520540000000002
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.209007072666545,
            "RMSE": 3.060196802253249,
            "R2": -1.8234356170996369,
            "Memory in Mb": 0.8641319274902344,
            "Time in s": 11.437965000000002
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.173565091899577,
            "RMSE": 2.996986036098964,
            "R2": -1.6456994146583188,
            "Memory in Mb": 0.9048995971679688,
            "Time in s": 12.395296000000002
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.1545102154576106,
            "RMSE": 2.9412312685847275,
            "R2": -1.494716293761022,
            "Memory in Mb": 0.9429206848144532,
            "Time in s": 13.397268000000002
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.1235341152888954,
            "RMSE": 2.885679937630878,
            "R2": -1.4055626483775598,
            "Memory in Mb": 0.9187583923339844,
            "Time in s": 14.455292000000002
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.0931325909773704,
            "RMSE": 2.8325152336083046,
            "R2": -1.3092471918321815,
            "Memory in Mb": 0.9785118103027344,
            "Time in s": 15.562633000000002
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.080423433010604,
            "RMSE": 2.7861157835692825,
            "R2": -1.2874470666919131,
            "Memory in Mb": 0.8416099548339844,
            "Time in s": 16.721025
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.0538460644054608,
            "RMSE": 2.73873459117484,
            "R2": -1.2649736085810763,
            "Memory in Mb": 0.9269638061523438,
            "Time in s": 17.931443
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.037762850657022,
            "RMSE": 2.6954140775252133,
            "R2": -1.1696179031883165,
            "Memory in Mb": 1.0152244567871094,
            "Time in s": 19.191903
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.022747434499167,
            "RMSE": 2.654976815796094,
            "R2": -1.0729218181826925,
            "Memory in Mb": 0.968769073486328,
            "Time in s": 20.501534
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 1.006861222675929,
            "RMSE": 2.615186194972241,
            "R2": -0.9736586966592728,
            "Memory in Mb": 0.803070068359375,
            "Time in s": 21.860299
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.9869414277387362,
            "RMSE": 2.5762284524749504,
            "R2": -0.9015227260176624,
            "Memory in Mb": 0.7759437561035156,
            "Time in s": 23.260671
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.966244541930286,
            "RMSE": 2.538677410892474,
            "R2": -0.8756731719459285,
            "Memory in Mb": 0.8428535461425781,
            "Time in s": 24.702724
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.9583039577617944,
            "RMSE": 2.5060806369029174,
            "R2": -0.8758219540617476,
            "Memory in Mb": 0.9465827941894532,
            "Time in s": 26.183847
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.9436352676783604,
            "RMSE": 2.472672874668102,
            "R2": -0.8662636043278715,
            "Memory in Mb": 1.0379486083984375,
            "Time in s": 27.712492
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.9279533445219876,
            "RMSE": 2.44025252932111,
            "R2": -0.816552178803118,
            "Memory in Mb": 1.1120071411132812,
            "Time in s": 29.286906
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.9160723193407864,
            "RMSE": 2.4102496967776017,
            "R2": -0.7913569678512289,
            "Memory in Mb": 1.17376708984375,
            "Time in s": 30.91286
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8969957702252379,
            "RMSE": 2.379401465215729,
            "R2": -0.753616871824967,
            "Memory in Mb": 1.2616004943847656,
            "Time in s": 32.587144
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8879951793456313,
            "RMSE": 2.351379467833174,
            "R2": -0.7280439441517783,
            "Memory in Mb": 1.355243682861328,
            "Time in s": 34.314383
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8778121160020841,
            "RMSE": 2.323761508818731,
            "R2": -0.7062232791684944,
            "Memory in Mb": 1.4321250915527344,
            "Time in s": 36.09551
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8674818777939237,
            "RMSE": 2.297554956673723,
            "R2": -0.683441607427212,
            "Memory in Mb": 1.4874954223632812,
            "Time in s": 37.948423
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8596582290799093,
            "RMSE": 2.2724190258224723,
            "R2": -0.6439714465644337,
            "Memory in Mb": 1.5595359802246094,
            "Time in s": 39.857894
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8554226716886886,
            "RMSE": 2.248810009475745,
            "R2": -0.601989379910626,
            "Memory in Mb": 1.6191024780273438,
            "Time in s": 41.823765
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8440517106498798,
            "RMSE": 2.2244180426447486,
            "R2": -0.5740310312005918,
            "Memory in Mb": 1.1261253356933594,
            "Time in s": 43.8642
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8347159483348575,
            "RMSE": 2.201058546919984,
            "R2": -0.5664676720057789,
            "Memory in Mb": 1.1678504943847656,
            "Time in s": 45.946931000000006
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8262269751007542,
            "RMSE": 2.1790511985851078,
            "R2": -0.5483240613297584,
            "Memory in Mb": 1.119964599609375,
            "Time in s": 48.07255500000001
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.8159800926650994,
            "RMSE": 2.1571455676024542,
            "R2": -0.5332153251602936,
            "Memory in Mb": 1.1733894348144531,
            "Time in s": 50.238479000000005
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.80675324923832,
            "RMSE": 2.1360469188887925,
            "R2": -0.5325676025464574,
            "Memory in Mb": 1.2283477783203125,
            "Time in s": 52.4464
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Adaptive Random Forest",
            "dataset": "TrumpApproval",
            "MAE": 0.801132918984696,
            "RMSE": 2.116027645482028,
            "R2": -0.5292923269414216,
            "Memory in Mb": 1.2836189270019531,
            "Time in s": 54.694244000000005
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 4.664574314574316,
            "RMSE": 12.7079745317607,
            "R2": -206.87879383707747,
            "Memory in Mb": 0.0196142196655273,
            "Time in s": 0.002799
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 2.767694704637076,
            "RMSE": 9.018587183866767,
            "R2": -85.14025986830408,
            "Memory in Mb": 0.0211782455444335,
            "Time in s": 0.009348
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 2.3093367298127023,
            "RMSE": 7.420500566500976,
            "R2": -37.24267181629702,
            "Memory in Mb": 0.0263471603393554,
            "Time in s": 0.018276
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 1.892363968348808,
            "RMSE": 6.441521936619904,
            "R2": -31.668094594906044,
            "Memory in Mb": 0.0274343490600585,
            "Time in s": 0.0297909999999999
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 2.1129412159858934,
            "RMSE": 6.114058653243701,
            "R2": -6.297346571779499,
            "Memory in Mb": 0.0340337753295898,
            "Time in s": 0.044022
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 2.832849782567835,
            "RMSE": 6.236602142425367,
            "R2": -2.2730130120415795,
            "Memory in Mb": 0.043257713317871,
            "Time in s": 0.061336
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 3.4069290990236856,
            "RMSE": 6.402381882180361,
            "R2": -1.3118663438824,
            "Memory in Mb": 0.0494871139526367,
            "Time in s": 0.082289
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 3.650377971160808,
            "RMSE": 6.321189272940957,
            "R2": -1.043267371916866,
            "Memory in Mb": 0.0551328659057617,
            "Time in s": 0.107232
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 4.035631404360372,
            "RMSE": 6.4483291916176695,
            "R2": -0.7783857772357967,
            "Memory in Mb": 0.0562467575073242,
            "Time in s": 0.136317
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 4.693189868957898,
            "RMSE": 7.0697740144659305,
            "R2": -0.4927792786841307,
            "Memory in Mb": 0.0576238632202148,
            "Time in s": 0.169599
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.274396860168236,
            "RMSE": 7.6542276724395,
            "R2": -0.3476225254437259,
            "Memory in Mb": 0.0577573776245117,
            "Time in s": 0.206842
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.247611065864998,
            "RMSE": 7.56430675955835,
            "R2": -0.0756815066101803,
            "Memory in Mb": 0.0578107833862304,
            "Time in s": 0.2481519999999999
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.084413296044263,
            "RMSE": 7.343803904848652,
            "R2": 0.1787885014844915,
            "Memory in Mb": 0.058394432067871,
            "Time in s": 0.2937619999999999
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 4.973008915037768,
            "RMSE": 7.173430375731751,
            "R2": 0.3340904988080935,
            "Memory in Mb": 0.0584478378295898,
            "Time in s": 0.343499
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.201973475639973,
            "RMSE": 7.389818367745889,
            "R2": 0.4319135436678196,
            "Memory in Mb": 0.0584478378295898,
            "Time in s": 0.397279
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.377897753885034,
            "RMSE": 7.538080975572278,
            "R2": 0.5233859928595415,
            "Memory in Mb": 0.0590581893920898,
            "Time in s": 0.455134
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.414777515271245,
            "RMSE": 7.541781669769663,
            "R2": 0.6093812059493195,
            "Memory in Mb": 0.0591115951538085,
            "Time in s": 0.517245
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.40059238519783,
            "RMSE": 7.511878220104288,
            "R2": 0.6917410630009373,
            "Memory in Mb": 0.0590581893920898,
            "Time in s": 0.583523
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 5.933708937482518,
            "RMSE": 9.717098931216649,
            "R2": 0.5747798982216288,
            "Memory in Mb": 0.0252752304077148,
            "Time in s": 0.662886
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 6.498767742677896,
            "RMSE": 10.515698120348512,
            "R2": 0.5640139167754625,
            "Memory in Mb": 0.0314245223999023,
            "Time in s": 0.744596
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 6.70504504336628,
            "RMSE": 10.67374680573752,
            "R2": 0.6157790851383267,
            "Memory in Mb": 0.0365400314331054,
            "Time in s": 0.828906
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 7.118759598962231,
            "RMSE": 11.248237924166032,
            "R2": 0.6566609789141779,
            "Memory in Mb": 0.0410718917846679,
            "Time in s": 0.916125
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 7.339750662382254,
            "RMSE": 11.39871112384624,
            "R2": 0.6937739359440155,
            "Memory in Mb": 0.0445966720581054,
            "Time in s": 1.006337
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 7.866457552558359,
            "RMSE": 12.301057885719082,
            "R2": 0.6741619364384577,
            "Memory in Mb": 0.0447034835815429,
            "Time in s": 1.099545
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 8.421243223038738,
            "RMSE": 13.285884557144795,
            "R2": 0.6655331879845522,
            "Memory in Mb": 0.0447034835815429,
            "Time in s": 1.19574
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 8.956033363560122,
            "RMSE": 14.109625220244896,
            "R2": 0.6732762786849746,
            "Memory in Mb": 0.0452070236206054,
            "Time in s": 1.295357
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 9.573413802719209,
            "RMSE": 14.887232530340055,
            "R2": 0.6845415314559343,
            "Memory in Mb": 0.0452337265014648,
            "Time in s": 1.398184
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 10.140823162094344,
            "RMSE": 15.798657858475249,
            "R2": 0.6835926538539661,
            "Memory in Mb": 0.0452604293823242,
            "Time in s": 1.504001
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 11.05646041165176,
            "RMSE": 17.826108509419473,
            "R2": 0.6344480842540857,
            "Memory in Mb": 0.0452604293823242,
            "Time in s": 1.6128270000000002
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 11.706749123156325,
            "RMSE": 18.647901518188576,
            "R2": 0.6576594092850414,
            "Memory in Mb": 0.0452871322631835,
            "Time in s": 1.7247210000000002
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 11.849547188265053,
            "RMSE": 18.683751607733637,
            "R2": 0.6922705096711406,
            "Memory in Mb": 0.0452871322631835,
            "Time in s": 1.839831
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 11.96088648820193,
            "RMSE": 18.74329807265456,
            "R2": 0.7184745225672177,
            "Memory in Mb": 0.0452871322631835,
            "Time in s": 1.958081
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 12.783089048199372,
            "RMSE": 19.95838853158221,
            "R2": 0.6900311672733117,
            "Memory in Mb": 0.0453138351440429,
            "Time in s": 2.0793790000000003
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 13.27307991721093,
            "RMSE": 20.988857849066505,
            "R2": 0.6848686892374445,
            "Memory in Mb": 0.0453405380249023,
            "Time in s": 2.203704
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 13.623649100869688,
            "RMSE": 21.545378780740656,
            "R2": 0.7062071700264252,
            "Memory in Mb": 0.0453405380249023,
            "Time in s": 2.331151
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 13.714864044781413,
            "RMSE": 21.4916185882578,
            "R2": 0.7274352207736796,
            "Memory in Mb": 0.0453405380249023,
            "Time in s": 2.4617500000000003
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 14.57407318940339,
            "RMSE": 22.90334645043852,
            "R2": 0.712266679293069,
            "Memory in Mb": 0.0456800460815429,
            "Time in s": 2.5991990000000005
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 15.311297276648313,
            "RMSE": 24.25392212062312,
            "R2": 0.6971079497894322,
            "Memory in Mb": 0.0457334518432617,
            "Time in s": 2.7396560000000005
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 15.833945440380871,
            "RMSE": 25.12811892959106,
            "R2": 0.7110893860103431,
            "Memory in Mb": 0.0457334518432617,
            "Time in s": 2.8832220000000004
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 15.995632485589844,
            "RMSE": 25.20571130808328,
            "R2": 0.7298778762133054,
            "Memory in Mb": 0.0456533432006835,
            "Time in s": 3.0299210000000003
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 16.482571154231422,
            "RMSE": 25.77399383544894,
            "R2": 0.7295670550023294,
            "Memory in Mb": 0.0461835861206054,
            "Time in s": 3.179584
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 17.556958821758087,
            "RMSE": 27.82207110996992,
            "R2": 0.7040173234911381,
            "Memory in Mb": 0.0469274520874023,
            "Time in s": 3.3322830000000003
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 18.31809908164516,
            "RMSE": 29.103026344234387,
            "R2": 0.7140266770057507,
            "Memory in Mb": 0.046980857849121,
            "Time in s": 3.488055
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 18.645508344467764,
            "RMSE": 29.39095020592674,
            "R2": 0.7243229903014706,
            "Memory in Mb": 0.0469541549682617,
            "Time in s": 3.646969
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 19.076944683969508,
            "RMSE": 29.900823849283483,
            "R2": 0.7315970559213162,
            "Memory in Mb": 0.0469007492065429,
            "Time in s": 3.808963
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 19.9412049113122,
            "RMSE": 31.299098765867257,
            "R2": 0.7144549629170223,
            "Memory in Mb": 0.046980857849121,
            "Time in s": 3.97409
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 20.652539482762663,
            "RMSE": 32.28122969713156,
            "R2": 0.7133599532452177,
            "Memory in Mb": 0.0470075607299804,
            "Time in s": 4.142383000000001
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 21.437431132207102,
            "RMSE": 33.471760575953454,
            "R2": 0.7229272102715563,
            "Memory in Mb": 0.0470075607299804,
            "Time in s": 4.313758000000001
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 21.589008276225865,
            "RMSE": 33.459905509370415,
            "R2": 0.7345566785536845,
            "Memory in Mb": 0.0470075607299804,
            "Time in s": 4.488246000000001
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 22.551700866868885,
            "RMSE": 35.03737693702089,
            "R2": 0.717908278090669,
            "Memory in Mb": 0.0470342636108398,
            "Time in s": 4.665796000000001
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 23.243872726229487,
            "RMSE": 35.949191367533466,
            "R2": 0.7160216409608307,
            "Memory in Mb": 0.0470075607299804,
            "Time in s": 4.846464000000001
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "ChickWeights",
            "MAE": 24.092513885911806,
            "RMSE": 37.13693189688246,
            "R2": 0.7196752558485364,
            "Memory in Mb": 0.0469541549682617,
            "Time in s": 5.030284000000001
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 2.695184981652336,
            "RMSE": 9.807184976514188,
            "R2": -224.6021011118197,
            "Memory in Mb": 0.0538091659545898,
            "Time in s": 0.005953
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 2.3994713447037435,
            "RMSE": 7.102066178895935,
            "R2": -19.27845129783118,
            "Memory in Mb": 0.0761518478393554,
            "Time in s": 0.016156
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.8170744682035584,
            "RMSE": 5.815253847056423,
            "R2": -17.329373299766118,
            "Memory in Mb": 0.0883970260620117,
            "Time in s": 0.0302489999999999
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.604995404573344,
            "RMSE": 5.081770494168446,
            "R2": -13.040545957103586,
            "Memory in Mb": 0.0980443954467773,
            "Time in s": 0.0484799999999999
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.824259078948539,
            "RMSE": 4.70488333223354,
            "R2": -6.5512954222403845,
            "Memory in Mb": 0.1071348190307617,
            "Time in s": 0.071134
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.918744608116588,
            "RMSE": 4.412336880489357,
            "R2": -4.634185300646759,
            "Memory in Mb": 0.1113233566284179,
            "Time in s": 0.098322
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.8761207739327503,
            "RMSE": 4.13187920011476,
            "R2": -4.105616799680584,
            "Memory in Mb": 0.1133375167846679,
            "Time in s": 0.13009
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.961232939518506,
            "RMSE": 3.976173487274506,
            "R2": -3.1695661963674864,
            "Memory in Mb": 0.1174459457397461,
            "Time in s": 0.166507
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 2.066134597500757,
            "RMSE": 3.873731518767916,
            "R2": -2.4756944369169624,
            "Memory in Mb": 0.1194601058959961,
            "Time in s": 0.207686
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 2.051125997923389,
            "RMSE": 3.731810291394655,
            "R2": -2.23527456693896,
            "Memory in Mb": 0.0176219940185546,
            "Time in s": 0.262943
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 2.0738811328897206,
            "RMSE": 4.417664564856108,
            "R2": -3.890594467356201,
            "Memory in Mb": 0.0358037948608398,
            "Time in s": 0.32065
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.9726100065438288,
            "RMSE": 4.237524240975239,
            "R2": -3.5337340888030546,
            "Memory in Mb": 0.0415029525756835,
            "Time in s": 0.38109
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.8594315384151243,
            "RMSE": 4.074751007989252,
            "R2": -3.248610147038553,
            "Memory in Mb": 0.0488462448120117,
            "Time in s": 0.444412
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.7773205119132678,
            "RMSE": 3.936654153117972,
            "R2": -3.1518424972300867,
            "Memory in Mb": 0.0637922286987304,
            "Time in s": 0.510957
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.8265705896173516,
            "RMSE": 3.8591002097544127,
            "R2": -2.923813511442849,
            "Memory in Mb": 0.0735006332397461,
            "Time in s": 0.581026
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.7437620649419607,
            "RMSE": 3.7394874649640353,
            "R2": -2.8667745903740336,
            "Memory in Mb": 0.0810804367065429,
            "Time in s": 0.6546050000000001
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.7029951846067328,
            "RMSE": 3.640753753244776,
            "R2": -2.873305462857122,
            "Memory in Mb": 0.0861959457397461,
            "Time in s": 0.7321480000000001
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.691125588823449,
            "RMSE": 3.557868621003357,
            "R2": -2.729329365262769,
            "Memory in Mb": 0.0937833786010742,
            "Time in s": 0.8137190000000001
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.641476039217788,
            "RMSE": 3.4678199943963026,
            "R2": -2.665503107324644,
            "Memory in Mb": 0.0988988876342773,
            "Time in s": 0.8994270000000001
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6260112424669562,
            "RMSE": 3.3952504336469187,
            "R2": -2.613000890937967,
            "Memory in Mb": 0.1061162948608398,
            "Time in s": 0.989373
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6289201270983786,
            "RMSE": 3.3343146523246907,
            "R2": -2.599793842225358,
            "Memory in Mb": 0.1101179122924804,
            "Time in s": 1.08339
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.667060123646852,
            "RMSE": 3.302206999442347,
            "R2": -2.466911261860751,
            "Memory in Mb": 0.1157636642456054,
            "Time in s": 1.1816330000000002
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.69667104754334,
            "RMSE": 3.2720484626443,
            "R2": -2.2278892819413008,
            "Memory in Mb": 0.1238470077514648,
            "Time in s": 1.2846220000000002
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6506098779434175,
            "RMSE": 3.2067821053781245,
            "R2": -2.029074572324324,
            "Memory in Mb": 0.1315069198608398,
            "Time in s": 1.3924660000000002
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6365240614669594,
            "RMSE": 3.1603547309397078,
            "R2": -1.8802784791951508,
            "Memory in Mb": 0.0784368515014648,
            "Time in s": 1.505205
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6536721067944389,
            "RMSE": 3.126560253923372,
            "R2": -1.823930193625598,
            "Memory in Mb": 0.0835790634155273,
            "Time in s": 1.621512
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6698160029512246,
            "RMSE": 3.0946441969309766,
            "R2": -1.7564325082786318,
            "Memory in Mb": 0.0873861312866211,
            "Time in s": 1.745676
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6408841434358417,
            "RMSE": 3.046586581366264,
            "R2": -1.735141389893172,
            "Memory in Mb": 0.0885534286499023,
            "Time in s": 1.8735
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6127327645791831,
            "RMSE": 2.999611374258061,
            "R2": -1.7170225021123482,
            "Memory in Mb": 0.0890569686889648,
            "Time in s": 2.004994
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6269498006919805,
            "RMSE": 2.973082395326553,
            "R2": -1.6396488808638732,
            "Memory in Mb": 0.0909147262573242,
            "Time in s": 2.140229
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.64112955570108,
            "RMSE": 2.949075530135499,
            "R2": -1.5576036781852802,
            "Memory in Mb": 0.0923452377319336,
            "Time in s": 2.27922
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6562657927450175,
            "RMSE": 2.9273758724267736,
            "R2": -1.4729982020585646,
            "Memory in Mb": 0.0944395065307617,
            "Time in s": 2.422009
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6610090165740414,
            "RMSE": 2.900076441293188,
            "R2": -1.409637238697782,
            "Memory in Mb": 0.0960302352905273,
            "Time in s": 2.568661
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.640070345532056,
            "RMSE": 2.8623424740678667,
            "R2": -1.3844340745604549,
            "Memory in Mb": 0.0981245040893554,
            "Time in s": 2.7190639999999995
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.6119603204138224,
            "RMSE": 2.8240252200668348,
            "R2": -1.381983091116742,
            "Memory in Mb": 0.1015691757202148,
            "Time in s": 2.8733429999999998
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.589173412563986,
            "RMSE": 2.788316481605285,
            "R2": -1.3731423466582644,
            "Memory in Mb": 0.1027364730834961,
            "Time in s": 3.031541
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.5872474989945902,
            "RMSE": 2.762320631839069,
            "R2": -1.3276973292362433,
            "Memory in Mb": 0.1038503646850586,
            "Time in s": 3.198810999999999
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.573860293324891,
            "RMSE": 2.731605449949154,
            "R2": -1.3008801881813965,
            "Memory in Mb": 0.1038503646850586,
            "Time in s": 3.3700799999999997
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.5672492734296428,
            "RMSE": 2.7047187411026274,
            "R2": -1.2659143323804294,
            "Memory in Mb": 0.1064214706420898,
            "Time in s": 3.5453349999999992
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.5527653312522924,
            "RMSE": 2.676901954415756,
            "R2": -1.2396196471003753,
            "Memory in Mb": 0.1070318222045898,
            "Time in s": 3.7247
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.5366430278321572,
            "RMSE": 2.648967131435787,
            "R2": -1.2172052322327516,
            "Memory in Mb": 0.1085958480834961,
            "Time in s": 3.908095
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.5234128351461855,
            "RMSE": 2.622526466573217,
            "R2": -1.1933402061449063,
            "Memory in Mb": 0.1101598739624023,
            "Time in s": 4.095543999999999
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.520997799745444,
            "RMSE": 2.601206078568585,
            "R2": -1.1541054380753062,
            "Memory in Mb": 0.1107702255249023,
            "Time in s": 4.287108999999999
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4988763963538276,
            "RMSE": 2.573388458013685,
            "R2": -1.0978034673380694,
            "Memory in Mb": 0.1112470626831054,
            "Time in s": 4.482816999999999
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4758663089418147,
            "RMSE": 2.54594713286987,
            "R2": -1.061955243276925,
            "Memory in Mb": 0.1116437911987304,
            "Time in s": 4.682644999999999
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.462937696730923,
            "RMSE": 2.523979038782575,
            "R2": -1.059822201667401,
            "Memory in Mb": 0.1116704940795898,
            "Time in s": 4.886850999999999
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4561394845136584,
            "RMSE": 2.50519739840106,
            "R2": -1.0464959899330828,
            "Memory in Mb": 0.1127042770385742,
            "Time in s": 5.100838999999999
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4393535919618172,
            "RMSE": 2.483254475687026,
            "R2": -1.0318268701719249,
            "Memory in Mb": 0.1132078170776367,
            "Time in s": 5.318975999999998
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4209594300543067,
            "RMSE": 2.4596960058574417,
            "R2": -1.0321742156649796,
            "Memory in Mb": 0.1138181686401367,
            "Time in s": 5.541285999999999
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Adaptive Model Rules",
            "dataset": "TrumpApproval",
            "MAE": 1.4020445673510784,
            "RMSE": 2.4364355463770164,
            "R2": -1.027485181852556,
            "Memory in Mb": 0.1144285202026367,
            "Time in s": 5.767785999999998
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 4.674710287324511,
            "RMSE": 12.709622005759083,
            "R2": -206.93269654300337,
            "Memory in Mb": 0.1438665390014648,
            "Time in s": 0.043578
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.741934273684416,
            "RMSE": 9.017856101646904,
            "R2": -85.12629469646626,
            "Memory in Mb": 0.1680784225463867,
            "Time in s": 0.114891
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.321314094852809,
            "RMSE": 7.424021720293775,
            "R2": -37.27897402435965,
            "Memory in Mb": 0.2096052169799804,
            "Time in s": 0.217395
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 1.9425031371298072,
            "RMSE": 6.446443185481759,
            "R2": -31.71802976156788,
            "Memory in Mb": 0.2417478561401367,
            "Time in s": 0.352059
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.220127898780405,
            "RMSE": 6.120501061993398,
            "R2": -6.312733162160137,
            "Memory in Mb": 0.3060827255249023,
            "Time in s": 0.516621
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.329752126186388,
            "RMSE": 5.733717860182345,
            "R2": -1.7664593315707076,
            "Memory in Mb": 0.3567266464233398,
            "Time in s": 0.719974
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.702798931003846,
            "RMSE": 5.8295610878248265,
            "R2": -0.9166874006339528,
            "Memory in Mb": 0.3732900619506836,
            "Time in s": 0.96062
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.6099619817757915,
            "RMSE": 5.526618942218035,
            "R2": -0.5618763668879856,
            "Memory in Mb": 0.4128637313842773,
            "Time in s": 1.239929
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.746820956366501,
            "RMSE": 5.433915350818854,
            "R2": -0.2628661224764999,
            "Memory in Mb": 0.4623746871948242,
            "Time in s": 1.563224
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 2.8880448046427323,
            "RMSE": 5.393209741308231,
            "R2": 0.131281330475993,
            "Memory in Mb": 0.5318593978881836,
            "Time in s": 1.933351
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.102793618966865,
            "RMSE": 5.4667968998241765,
            "R2": 0.312565398150165,
            "Memory in Mb": 0.5604543685913086,
            "Time in s": 2.356966
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.301393875206229,
            "RMSE": 5.777687225912497,
            "R2": 0.3724425463943938,
            "Memory in Mb": 0.1946859359741211,
            "Time in s": 2.834547
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.2818761969220303,
            "RMSE": 5.651296511520541,
            "R2": 0.5136946280960023,
            "Memory in Mb": 0.2288389205932617,
            "Time in s": 3.343438
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.2515588511167266,
            "RMSE": 5.538190901897615,
            "R2": 0.6030852117170243,
            "Memory in Mb": 0.2577199935913086,
            "Time in s": 3.884102
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.5490619378471253,
            "RMSE": 5.901472315915889,
            "R2": 0.6377005660204649,
            "Memory in Mb": 0.2627325057983398,
            "Time in s": 4.460716
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.748099204740288,
            "RMSE": 6.114989482363781,
            "R2": 0.6863562530103127,
            "Memory in Mb": 0.2941198348999023,
            "Time in s": 5.073099
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 3.855321751115436,
            "RMSE": 6.172883744230479,
            "R2": 0.7383134393857906,
            "Memory in Mb": 0.3320951461791992,
            "Time in s": 5.716163
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 4.064611732985858,
            "RMSE": 6.634154210053631,
            "R2": 0.7595694090278171,
            "Memory in Mb": 0.2527418136596679,
            "Time in s": 6.400463
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 4.2854283677061895,
            "RMSE": 7.034301545827039,
            "R2": 0.7771654635449772,
            "Memory in Mb": 0.3202161788940429,
            "Time in s": 7.116785
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 4.87812017832838,
            "RMSE": 8.464168223538273,
            "R2": 0.7175347810295998,
            "Memory in Mb": 0.3510808944702148,
            "Time in s": 7.873189
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 5.139510271881338,
            "RMSE": 8.709209118107985,
            "R2": 0.7441975817879227,
            "Memory in Mb": 0.3200139999389648,
            "Time in s": 8.671972
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 5.512568989147682,
            "RMSE": 9.214318878962654,
            "R2": 0.7696009669773758,
            "Memory in Mb": 0.3710927963256836,
            "Time in s": 9.508629
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 5.61462831814645,
            "RMSE": 9.300369065456374,
            "R2": 0.7961404678287027,
            "Memory in Mb": 0.4192609786987304,
            "Time in s": 10.381303
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 6.307820522062941,
            "RMSE": 10.632794713133398,
            "R2": 0.7565488951511344,
            "Memory in Mb": 0.3416013717651367,
            "Time in s": 11.288641
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 6.788015101176612,
            "RMSE": 11.834244259749068,
            "R2": 0.7346291964126817,
            "Memory in Mb": 0.3569021224975586,
            "Time in s": 12.231102
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 7.083325494446596,
            "RMSE": 12.279756566760542,
            "R2": 0.7525262008661281,
            "Memory in Mb": 0.3965520858764648,
            "Time in s": 13.20812
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 7.191320030958258,
            "RMSE": 12.343414248948324,
            "R2": 0.7831373025283351,
            "Memory in Mb": 0.4258260726928711,
            "Time in s": 14.218151
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 7.797209174725968,
            "RMSE": 13.278742843330225,
            "R2": 0.7764780945249113,
            "Memory in Mb": 0.4501142501831054,
            "Time in s": 15.260696
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 8.817827198046418,
            "RMSE": 15.9696940597815,
            "R2": 0.7066209046531168,
            "Memory in Mb": 0.4718656539916992,
            "Time in s": 16.339578
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 9.357743221083844,
            "RMSE": 16.830542617885925,
            "R2": 0.7211345584533546,
            "Memory in Mb": 0.3236379623413086,
            "Time in s": 17.459623999999998
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 9.597227793355117,
            "RMSE": 16.978620563243194,
            "R2": 0.7458759585671038,
            "Memory in Mb": 0.3676939010620117,
            "Time in s": 18.612921
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 9.7373515968392,
            "RMSE": 17.046818432657442,
            "R2": 0.7671306392320572,
            "Memory in Mb": 0.3629522323608398,
            "Time in s": 19.795535999999995
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 10.474784553852622,
            "RMSE": 18.420082712462506,
            "R2": 0.7359718490826586,
            "Memory in Mb": 0.3571195602416992,
            "Time in s": 21.012742
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 11.136965297216438,
            "RMSE": 20.001694167276444,
            "R2": 0.7138145773791849,
            "Memory in Mb": 0.3998785018920898,
            "Time in s": 22.263945
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 11.663755213802826,
            "RMSE": 20.72310945995512,
            "R2": 0.7282041838356077,
            "Memory in Mb": 0.3288450241088867,
            "Time in s": 23.553922
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 11.794892571100942,
            "RMSE": 20.71536814309967,
            "R2": 0.7467690419180344,
            "Memory in Mb": 0.4024953842163086,
            "Time in s": 24.874665
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 12.7361976076631,
            "RMSE": 22.396840643020628,
            "R2": 0.7248523596518419,
            "Memory in Mb": 0.4475545883178711,
            "Time in s": 26.248019
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 13.669165628181592,
            "RMSE": 24.17119440887557,
            "R2": 0.6991706950778176,
            "Memory in Mb": 0.4968290328979492,
            "Time in s": 27.657996
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 14.21091951782044,
            "RMSE": 24.907688885339496,
            "R2": 0.7161359437094021,
            "Memory in Mb": 0.5376424789428711,
            "Time in s": 29.100111
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 14.453337266265764,
            "RMSE": 25.002813963201465,
            "R2": 0.7342091543116155,
            "Memory in Mb": 0.5657072067260742,
            "Time in s": 30.577019
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 14.795462221424788,
            "RMSE": 25.396591749368834,
            "R2": 0.7374288341656263,
            "Memory in Mb": 0.2583265304565429,
            "Time in s": 32.092868
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 16.121556592117344,
            "RMSE": 28.147488646444906,
            "R2": 0.6970529793362255,
            "Memory in Mb": 0.3047628402709961,
            "Time in s": 33.634783000000006
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 16.919755395139642,
            "RMSE": 29.31210430009691,
            "R2": 0.7099030173412568,
            "Memory in Mb": 0.3544912338256836,
            "Time in s": 35.20760200000001
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 17.222944705236912,
            "RMSE": 29.519121223412064,
            "R2": 0.7219133474565596,
            "Memory in Mb": 0.3983259201049804,
            "Time in s": 36.808400000000006
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 17.875632407347712,
            "RMSE": 30.34841895302658,
            "R2": 0.7235012910446976,
            "Memory in Mb": 0.4324254989624023,
            "Time in s": 38.43633400000001
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 18.888217233083253,
            "RMSE": 31.835585198521954,
            "R2": 0.7045822227904736,
            "Memory in Mb": 0.4678411483764648,
            "Time in s": 40.09290200000001
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 19.824673890348247,
            "RMSE": 33.232962754926376,
            "R2": 0.6962090391160322,
            "Memory in Mb": 0.4975500106811523,
            "Time in s": 41.78457100000001
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 20.55396214529221,
            "RMSE": 34.09704280994323,
            "R2": 0.712478586733055,
            "Memory in Mb": 0.5351285934448242,
            "Time in s": 43.50851800000001
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 20.794926737672743,
            "RMSE": 34.209729391662115,
            "R2": 0.7225264054992676,
            "Memory in Mb": 0.576685905456543,
            "Time in s": 45.26814300000001
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 21.840113545070352,
            "RMSE": 36.13121679398973,
            "R2": 0.7000199686285788,
            "Memory in Mb": 0.4753904342651367,
            "Time in s": 47.07007900000001
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 22.59682566601873,
            "RMSE": 37.08324430393829,
            "R2": 0.6978222813826447,
            "Memory in Mb": 0.5189352035522461,
            "Time in s": 48.90757000000001
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "ChickWeights",
            "MAE": 23.516206925607506,
            "RMSE": 38.207190389030345,
            "R2": 0.703284935102584,
            "Memory in Mb": 0.5585355758666992,
            "Time in s": 50.782863000000006
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 2.677140920600926,
            "RMSE": 9.804891856735376,
            "R2": -224.4966127051096,
            "Memory in Mb": 0.2373647689819336,
            "Time in s": 0.10297
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 2.227777813220112,
            "RMSE": 7.083306817310631,
            "R2": -19.171465983096805,
            "Memory in Mb": 0.3270711898803711,
            "Time in s": 0.289755
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.615301860635012,
            "RMSE": 5.7908261762165685,
            "R2": -17.175707266102673,
            "Memory in Mb": 0.3493108749389648,
            "Time in s": 0.561259
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.3541232617236425,
            "RMSE": 5.026566774725167,
            "R2": -12.73715546617699,
            "Memory in Mb": 0.3968191146850586,
            "Time in s": 0.918423
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.2177336486572592,
            "RMSE": 4.516233376106315,
            "R2": -5.957872973758095,
            "Memory in Mb": 0.4107885360717773,
            "Time in s": 1.362708
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.1154353306650455,
            "RMSE": 4.135716354504269,
            "R2": -3.949887064372274,
            "Memory in Mb": 0.4562673568725586,
            "Time in s": 1.881933
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.2694693870086102,
            "RMSE": 4.857381406328817,
            "R2": -6.05598089151511,
            "Memory in Mb": 0.2026891708374023,
            "Time in s": 2.479905
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.197729670480587,
            "RMSE": 4.553187715474859,
            "R2": -4.467532002416268,
            "Memory in Mb": 0.3215742111206054,
            "Time in s": 3.138645
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.1382354235034091,
            "RMSE": 4.302111654125532,
            "R2": -3.2869252353070264,
            "Memory in Mb": 0.4017667770385742,
            "Time in s": 3.869636
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.0619299314905082,
            "RMSE": 4.083716699099621,
            "R2": -2.874210730330613,
            "Memory in Mb": 0.4772901535034179,
            "Time in s": 4.674132999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 1.009898171671029,
            "RMSE": 3.898715068147509,
            "R2": -2.8090719143731837,
            "Memory in Mb": 0.5200605392456055,
            "Time in s": 5.552957999999999
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.9646445055554522,
            "RMSE": 3.736185930434801,
            "R2": -2.5244277699140394,
            "Memory in Mb": 0.590418815612793,
            "Time in s": 6.501358999999999
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.9172332240820484,
            "RMSE": 3.59133014967386,
            "R2": -2.300314999970906,
            "Memory in Mb": 0.677699089050293,
            "Time in s": 7.522147999999999
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8713372213927624,
            "RMSE": 3.461793231901636,
            "R2": -2.2106176891844487,
            "Memory in Mb": 0.7459287643432617,
            "Time in s": 8.615362
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8589405406556339,
            "RMSE": 3.350216865329824,
            "R2": -1.9572094631572516,
            "Memory in Mb": 0.8300580978393555,
            "Time in s": 9.791068
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8332253596869799,
            "RMSE": 3.2462964384589745,
            "R2": -1.91407713381932,
            "Memory in Mb": 0.8134641647338867,
            "Time in s": 11.051061
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8452804825423809,
            "RMSE": 3.1781241500612394,
            "R2": -1.9514868559348704,
            "Memory in Mb": 0.7938528060913086,
            "Time in s": 12.398121
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8633895166787324,
            "RMSE": 3.1040171399305283,
            "R2": -1.8385669899509445,
            "Memory in Mb": 0.8660383224487305,
            "Time in s": 13.839894
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8513159306308952,
            "RMSE": 3.0258511220091995,
            "R2": -1.790715802132521,
            "Memory in Mb": 0.930495262145996,
            "Time in s": 15.372487
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8510161564157176,
            "RMSE": 2.9641796059686003,
            "R2": -1.7538068241726803,
            "Memory in Mb": 0.9046812057495116,
            "Time in s": 17.004842
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8518447067444684,
            "RMSE": 2.91289276041272,
            "R2": -1.747346648183163,
            "Memory in Mb": 0.2984609603881836,
            "Time in s": 18.737382
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8395925714721912,
            "RMSE": 2.8496340177457244,
            "R2": -1.5817388594042834,
            "Memory in Mb": 0.3453207015991211,
            "Time in s": 20.534513
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8276812048623222,
            "RMSE": 2.790693875069675,
            "R2": -1.3480296319058032,
            "Memory in Mb": 0.3807516098022461,
            "Time in s": 22.405168
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.8089244758990292,
            "RMSE": 2.7333778802045163,
            "R2": -1.2007484949677454,
            "Memory in Mb": 0.4482488632202148,
            "Time in s": 24.346508
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7928829832001318,
            "RMSE": 2.679994202833863,
            "R2": -1.0712404739849797,
            "Memory in Mb": 0.4975194931030273,
            "Time in s": 26.364916
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7968627360462042,
            "RMSE": 2.655906961990266,
            "R2": -1.037727311679443,
            "Memory in Mb": 0.3753881454467773,
            "Time in s": 28.465481
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7742648164612971,
            "RMSE": 2.606576025481956,
            "R2": -0.9555400217068246,
            "Memory in Mb": 0.4063673019409179,
            "Time in s": 30.635854
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7686196547282114,
            "RMSE": 2.5632583130611786,
            "R2": -0.9361432250468024,
            "Memory in Mb": 0.4374494552612304,
            "Time in s": 32.873421
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7604339230100455,
            "RMSE": 2.522208925126442,
            "R2": -0.9209911676265596,
            "Memory in Mb": 0.4967718124389648,
            "Time in s": 35.174013
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7505205215384793,
            "RMSE": 2.4816305596178174,
            "R2": -0.839105014250833,
            "Memory in Mb": 0.569575309753418,
            "Time in s": 37.541938
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7415649894603582,
            "RMSE": 2.4434454055931187,
            "R2": -0.7557664113175795,
            "Memory in Mb": 0.6584272384643555,
            "Time in s": 39.976025
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7318408439896782,
            "RMSE": 2.406886195682516,
            "R2": -0.6717754169622376,
            "Memory in Mb": 0.7120962142944336,
            "Time in s": 42.479937
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7165688958291918,
            "RMSE": 2.37061113672817,
            "R2": -0.6101020988109156,
            "Memory in Mb": 0.8089780807495117,
            "Time in s": 45.058017
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7019759043195819,
            "RMSE": 2.336022363731008,
            "R2": -0.5881668313132071,
            "Memory in Mb": 0.8398160934448242,
            "Time in s": 47.720249
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.7046161229979929,
            "RMSE": 2.307765546298159,
            "R2": -0.5906876272832315,
            "Memory in Mb": 0.9275884628295898,
            "Time in s": 50.471651
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.699791115281057,
            "RMSE": 2.2802792890719745,
            "R2": -0.5871418479715558,
            "Memory in Mb": 0.9087285995483398,
            "Time in s": 53.310919
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6993154625867034,
            "RMSE": 2.2532668970074776,
            "R2": -0.5488294820654547,
            "Memory in Mb": 0.8719320297241211,
            "Time in s": 56.236366
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6904813287783395,
            "RMSE": 2.224703478329614,
            "R2": -0.5261679577762028,
            "Memory in Mb": 0.929518699645996,
            "Time in s": 59.248631
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6809571474431378,
            "RMSE": 2.1968956754751456,
            "R2": -0.4949206250779803,
            "Memory in Mb": 1.0446271896362305,
            "Time in s": 62.34821899999999
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6801944660295238,
            "RMSE": 2.1726014141558028,
            "R2": -0.4752630155166446,
            "Memory in Mb": 1.1031560897827148,
            "Time in s": 65.54039399999999
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6800251543540311,
            "RMSE": 2.1538267014914845,
            "R2": -0.4657984869085023,
            "Memory in Mb": 1.0328702926635742,
            "Time in s": 68.82165799999999
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6756860923792902,
            "RMSE": 2.1342936501586,
            "R2": -0.4526954783446735,
            "Memory in Mb": 0.7475957870483398,
            "Time in s": 72.18837399999998
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6733560632024954,
            "RMSE": 2.111426905397114,
            "R2": -0.4192847599850244,
            "Memory in Mb": 0.8119535446166992,
            "Time in s": 75.62699399999998
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6699617254268444,
            "RMSE": 2.0889651464935617,
            "R2": -0.3823451381863831,
            "Memory in Mb": 0.8655576705932617,
            "Time in s": 79.14156799999998
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6641763033522209,
            "RMSE": 2.070781028281848,
            "R2": -0.3641082228169974,
            "Memory in Mb": 0.8467855453491211,
            "Time in s": 82.73512999999998
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6581948551182502,
            "RMSE": 2.04921868376074,
            "R2": -0.3577970506072152,
            "Memory in Mb": 0.9400205612182616,
            "Time in s": 86.40810799999998
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6518145768911946,
            "RMSE": 2.0285221107553344,
            "R2": -0.3417959776408932,
            "Memory in Mb": 0.8168668746948242,
            "Time in s": 90.15720199999998
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6459384626205039,
            "RMSE": 2.0083339154310043,
            "R2": -0.328972794111009,
            "Memory in Mb": 0.9120321273803712,
            "Time in s": 93.98330699999998
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6434185155449816,
            "RMSE": 1.989534246313576,
            "R2": -0.3295384550375804,
            "Memory in Mb": 0.9782476425170898,
            "Time in s": 97.888458
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Streaming Random Patches",
            "dataset": "TrumpApproval",
            "MAE": 0.6405613133684143,
            "RMSE": 1.9713432953350207,
            "R2": -0.3273099653285773,
            "Memory in Mb": 1.0593442916870115,
            "Time in s": 101.872577
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 10.961585696594296,
            "RMSE": 17.742218537059934,
            "R2": -404.203665453531,
            "Memory in Mb": 0.1782550811767578,
            "Time in s": 0.00837
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 5.889263372306967,
            "RMSE": 12.56756036562654,
            "R2": -166.2750319368382,
            "Memory in Mb": 0.1910533905029297,
            "Time in s": 0.024461
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.385855416063054,
            "RMSE": 10.300574999811516,
            "R2": -72.68935558725912,
            "Memory in Mb": 0.2280941009521484,
            "Time in s": 0.04853
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 3.447994945519213,
            "RMSE": 8.931729546653537,
            "R2": -61.80843214992921,
            "Memory in Mb": 0.2438068389892578,
            "Time in s": 0.081553
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 3.35253400433443,
            "RMSE": 8.24824849102831,
            "R2": -12.280953122644297,
            "Memory in Mb": 0.2916851043701172,
            "Time in s": 0.123768
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 3.890626377385135,
            "RMSE": 8.046318086318358,
            "R2": -4.448112248710658,
            "Memory in Mb": 0.3612346649169922,
            "Time in s": 0.176552
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.3386080839549335,
            "RMSE": 7.968508799771546,
            "R2": -2.581242138287016,
            "Memory in Mb": 0.4169635772705078,
            "Time in s": 0.2426829999999999
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.490657725713863,
            "RMSE": 7.741140850532905,
            "R2": -2.064344233357061,
            "Memory in Mb": 0.4634113311767578,
            "Time in s": 0.322916
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.7848487383098295,
            "RMSE": 7.706963997319479,
            "R2": -1.5403773740733393,
            "Memory in Mb": 0.4844684600830078,
            "Time in s": 0.418203
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.819508170706054,
            "RMSE": 7.525876668153812,
            "R2": -0.6916040970280823,
            "Memory in Mb": 0.5139484405517578,
            "Time in s": 0.528794
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.831868630589585,
            "RMSE": 7.4067264415397105,
            "R2": -0.261880180240535,
            "Memory in Mb": 0.5271091461181641,
            "Time in s": 0.654758
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.689813959013141,
            "RMSE": 7.185628463196342,
            "R2": 0.0293225226637304,
            "Memory in Mb": 0.5355319976806641,
            "Time in s": 0.796727
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.575735548989308,
            "RMSE": 6.988996035323699,
            "R2": 0.2562234762018912,
            "Memory in Mb": 0.5445156097412109,
            "Time in s": 0.954849
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.5047654468276,
            "RMSE": 6.840884466051986,
            "R2": 0.3943998861813385,
            "Memory in Mb": 0.5490932464599609,
            "Time in s": 1.128949
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.788922390491115,
            "RMSE": 7.112527411058041,
            "R2": 0.4737467226899117,
            "Memory in Mb": 0.5519008636474609,
            "Time in s": 1.318602
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 4.970710142849908,
            "RMSE": 7.252656159084941,
            "R2": 0.5587960603089545,
            "Memory in Mb": 0.5291376113891602,
            "Time in s": 1.527133
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 5.027942129925975,
            "RMSE": 7.276897995624471,
            "R2": 0.6363381045701173,
            "Memory in Mb": 0.5012483596801758,
            "Time in s": 1.7549830000000002
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 5.049038224539579,
            "RMSE": 7.28413559977408,
            "R2": 0.7101491068659838,
            "Memory in Mb": 0.3717927932739258,
            "Time in s": 2.012416
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 5.250417000807892,
            "RMSE": 7.635375364934655,
            "R2": 0.7374564682191251,
            "Memory in Mb": 0.3473329544067383,
            "Time in s": 2.287127
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 5.8380227010176045,
            "RMSE": 8.722095838276593,
            "R2": 0.7000574251839753,
            "Memory in Mb": 0.3545808792114258,
            "Time in s": 2.575553
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 6.044258003678201,
            "RMSE": 8.960072203538655,
            "R2": 0.7292489015049135,
            "Memory in Mb": 0.391514778137207,
            "Time in s": 2.875072
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 6.276524828158362,
            "RMSE": 9.354066864400572,
            "R2": 0.7625593259413487,
            "Memory in Mb": 0.4183511734008789,
            "Time in s": 3.187566
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 6.3739207187481774,
            "RMSE": 9.482128758285446,
            "R2": 0.7880944389945109,
            "Memory in Mb": 0.4399347305297851,
            "Time in s": 3.512786
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 6.979732945669537,
            "RMSE": 10.70081988088543,
            "R2": 0.7534238884125567,
            "Memory in Mb": 0.4525842666625976,
            "Time in s": 3.851311
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 7.440978636214291,
            "RMSE": 11.778455343325094,
            "R2": 0.7371253175053303,
            "Memory in Mb": 0.4610300064086914,
            "Time in s": 4.203753
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 7.722695321089189,
            "RMSE": 12.251182899165162,
            "R2": 0.7536765505554787,
            "Memory in Mb": 0.4700403213500976,
            "Time in s": 4.570129
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 7.706764271589622,
            "RMSE": 12.242915074252831,
            "R2": 0.7866542868859879,
            "Memory in Mb": 0.4733209609985351,
            "Time in s": 4.950063
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 8.246398153738868,
            "RMSE": 13.148346181255995,
            "R2": 0.7808464902384371,
            "Memory in Mb": 0.4770059585571289,
            "Time in s": 5.342659
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 9.3474227240372,
            "RMSE": 15.837966045238383,
            "R2": 0.7114408913609181,
            "Memory in Mb": 0.4802255630493164,
            "Time in s": 5.749268000000001
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 9.81720525198044,
            "RMSE": 16.4984558080814,
            "R2": 0.732030690326682,
            "Memory in Mb": 0.4911470413208008,
            "Time in s": 6.171356000000001
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 10.029686613445753,
            "RMSE": 16.618597428793866,
            "R2": 0.7565388422982208,
            "Memory in Mb": 0.496312141418457,
            "Time in s": 6.607662000000001
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 10.183424974922596,
            "RMSE": 16.72954607175143,
            "R2": 0.7757182197717174,
            "Memory in Mb": 0.5041093826293945,
            "Time in s": 7.058783000000001
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 11.087226456936444,
            "RMSE": 18.183293641227465,
            "R2": 0.7427163510168195,
            "Memory in Mb": 0.5065813064575195,
            "Time in s": 7.524030000000001
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 11.611208342142504,
            "RMSE": 19.353368352464965,
            "R2": 0.7320664683002076,
            "Memory in Mb": 0.4931306838989258,
            "Time in s": 8.007171000000001
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 12.01727910935522,
            "RMSE": 20.0211446068419,
            "R2": 0.7463056879958478,
            "Memory in Mb": 0.4681062698364258,
            "Time in s": 8.510702000000002
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 12.181393533243163,
            "RMSE": 20.04691533881536,
            "R2": 0.7628481050767555,
            "Memory in Mb": 0.4353647232055664,
            "Time in s": 9.035917
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 13.09061742270854,
            "RMSE": 21.647454224788547,
            "R2": 0.7429569103775002,
            "Memory in Mb": 0.4253015518188476,
            "Time in s": 9.583169000000002
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 13.857583790923206,
            "RMSE": 23.134723844753264,
            "R2": 0.7244169153448246,
            "Memory in Mb": 0.4488153457641601,
            "Time in s": 10.147004
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 14.415812868423222,
            "RMSE": 24.06086703427245,
            "R2": 0.7351096813998451,
            "Memory in Mb": 0.4820413589477539,
            "Time in s": 10.724926
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 14.633210713365676,
            "RMSE": 24.14605091357361,
            "R2": 0.7521125932778163,
            "Memory in Mb": 0.5092172622680664,
            "Time in s": 11.318068
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 15.133020029766048,
            "RMSE": 24.73830229788057,
            "R2": 0.7508643131645836,
            "Memory in Mb": 0.5367746353149414,
            "Time in s": 11.926425
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 16.308165732303497,
            "RMSE": 27.095114472384648,
            "R2": 0.7192825818530082,
            "Memory in Mb": 0.5905351638793945,
            "Time in s": 12.55391
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 17.097647362788752,
            "RMSE": 28.42746345262044,
            "R2": 0.7271490710401121,
            "Memory in Mb": 0.6096200942993164,
            "Time in s": 13.198999
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 17.403233741388874,
            "RMSE": 28.60630060223112,
            "R2": 0.7388459944901757,
            "Memory in Mb": 0.6277017593383789,
            "Time in s": 13.862263
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 17.845914876737442,
            "RMSE": 29.12415998011611,
            "R2": 0.7453593218363636,
            "Memory in Mb": 0.6518182754516602,
            "Time in s": 14.54413
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 18.74953553887996,
            "RMSE": 30.62874049978988,
            "R2": 0.7265554777237875,
            "Memory in Mb": 0.6593713760375977,
            "Time in s": 15.245298000000002
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 19.47487310339954,
            "RMSE": 31.618292560451803,
            "R2": 0.7250121198400961,
            "Memory in Mb": 0.6093225479125977,
            "Time in s": 15.967903000000002
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 20.25384975920148,
            "RMSE": 32.7838221306768,
            "R2": 0.7341994138392889,
            "Memory in Mb": 0.6206216812133789,
            "Time in s": 16.707851
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 20.43401222967888,
            "RMSE": 32.81136182644564,
            "R2": 0.7447469767293837,
            "Memory in Mb": 0.6340532302856445,
            "Time in s": 17.46759
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 21.48271816680656,
            "RMSE": 34.486522216355176,
            "R2": 0.7267085961280999,
            "Memory in Mb": 0.6409807205200195,
            "Time in s": 18.246304
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 22.214948014440758,
            "RMSE": 35.44362766111904,
            "R2": 0.7239528137855742,
            "Memory in Mb": 0.6374177932739258,
            "Time in s": 19.046772
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "ChickWeights",
            "MAE": 23.05953013824058,
            "RMSE": 36.58622235196899,
            "R2": 0.7279275728793118,
            "Memory in Mb": 0.6435747146606445,
            "Time in s": 19.865794
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 6.585839365171216,
            "RMSE": 13.881516159864546,
            "R2": -450.9893611410228,
            "Memory in Mb": 0.4141368865966797,
            "Time in s": 0.017776
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 4.363712565198605,
            "RMSE": 9.938671227284791,
            "R2": -38.712022235644,
            "Memory in Mb": 0.5953998565673828,
            "Time in s": 0.05778
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 3.1246200328296143,
            "RMSE": 8.126568674182735,
            "R2": -34.79519075888522,
            "Memory in Mb": 0.7211894989013672,
            "Time in s": 0.123528
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.5854221987839483,
            "RMSE": 7.070456887280416,
            "R2": -26.179962781345687,
            "Memory in Mb": 0.8254451751708984,
            "Time in s": 0.217362
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.612795341566278,
            "RMSE": 6.441452396131832,
            "R2": -13.15439617190778,
            "Memory in Mb": 0.9287128448486328,
            "Time in s": 0.340609
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.5650159676967723,
            "RMSE": 5.964319967024998,
            "R2": -9.294746752112973,
            "Memory in Mb": 0.9687213897705078,
            "Time in s": 0.493962
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.4246087892523565,
            "RMSE": 5.555151474129083,
            "R2": -8.228790661275799,
            "Memory in Mb": 0.9892597198486328,
            "Time in s": 0.677921
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.2372944440918734,
            "RMSE": 5.2113826313001965,
            "R2": -6.162524907472281,
            "Memory in Mb": 1.0282306671142578,
            "Time in s": 0.8947890000000001
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 2.1466345389477697,
            "RMSE": 4.9537003451084844,
            "R2": -4.683842281929501,
            "Memory in Mb": 0.9880685806274414,
            "Time in s": 1.151076
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.9892950861944356,
            "RMSE": 4.704683592711833,
            "R2": -4.14200943628533,
            "Memory in Mb": 0.5611734390258789,
            "Time in s": 1.477073
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.8962186057938932,
            "RMSE": 4.499134208858052,
            "R2": -4.072640393025983,
            "Memory in Mb": 0.3967218399047851,
            "Time in s": 1.841739
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.803503053095204,
            "RMSE": 4.314740779926486,
            "R2": -3.700467691841136,
            "Memory in Mb": 0.4504899978637695,
            "Time in s": 2.225753
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.7080100607704198,
            "RMSE": 4.14999374436193,
            "R2": -3.406965132392963,
            "Memory in Mb": 0.5133523941040039,
            "Time in s": 2.631091
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.6655932342441322,
            "RMSE": 4.017842470146439,
            "R2": -3.324861014485008,
            "Memory in Mb": 0.6190156936645508,
            "Time in s": 3.0590589999999995
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.6385421968346507,
            "RMSE": 3.904974440220909,
            "R2": -3.01765496812087,
            "Memory in Mb": 0.7099161148071289,
            "Time in s": 3.510991
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.5504197008133211,
            "RMSE": 3.781681667850968,
            "R2": -2.954527764504537,
            "Memory in Mb": 0.777043342590332,
            "Time in s": 3.987728
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.5047182142648992,
            "RMSE": 3.6774767295200856,
            "R2": -2.9518368180177696,
            "Memory in Mb": 0.8162164688110352,
            "Time in s": 4.49124
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.5167434089128324,
            "RMSE": 3.599404249538014,
            "R2": -2.816912258630976,
            "Memory in Mb": 0.8943338394165039,
            "Time in s": 5.022537
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.47690532831993,
            "RMSE": 3.5095784857397434,
            "R2": -2.754312484791544,
            "Memory in Mb": 0.9456682205200196,
            "Time in s": 5.582067
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.4473785178172314,
            "RMSE": 3.4281100357630656,
            "R2": -2.683273334840131,
            "Memory in Mb": 1.0103578567504885,
            "Time in s": 6.172723
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.40955398667131,
            "RMSE": 3.3497394826483737,
            "R2": -2.633176800681623,
            "Memory in Mb": 0.9896020889282228,
            "Time in s": 6.801780999999999
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.3766290707405415,
            "RMSE": 3.2780180874471507,
            "R2": -2.4163065189839363,
            "Memory in Mb": 1.0508508682250977,
            "Time in s": 7.462708999999999
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.3473843223583597,
            "RMSE": 3.2105206765417766,
            "R2": -2.1076358108912725,
            "Memory in Mb": 1.1290063858032229,
            "Time in s": 8.158304
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.3146601146346069,
            "RMSE": 3.145698486393554,
            "R2": -1.914776430829721,
            "Memory in Mb": 1.2007226943969729,
            "Time in s": 8.887782
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.2829933656636,
            "RMSE": 3.084835387092109,
            "R2": -1.7442697801193798,
            "Memory in Mb": 1.2468271255493164,
            "Time in s": 9.6533
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.253253159364902,
            "RMSE": 3.027195393916086,
            "R2": -1.647288417049146,
            "Memory in Mb": 1.2976083755493164,
            "Time in s": 10.456286
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.221748892460797,
            "RMSE": 2.9719574458877616,
            "R2": -1.5422080467663055,
            "Memory in Mb": 1.2989130020141602,
            "Time in s": 11.302161
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.2084725532442826,
            "RMSE": 2.924408360153415,
            "R2": -1.5201637785773734,
            "Memory in Mb": 1.2362565994262695,
            "Time in s": 12.194852
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.1798260089354875,
            "RMSE": 2.875143807222344,
            "R2": -1.496217338554359,
            "Memory in Mb": 1.0948266983032229,
            "Time in s": 13.14623
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.1697523000107772,
            "RMSE": 2.832108990371036,
            "R2": -1.3952574337441268,
            "Memory in Mb": 0.9711389541625975,
            "Time in s": 14.161435
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.1550049446613664,
            "RMSE": 2.791430677298195,
            "R2": -1.29147514335963,
            "Memory in Mb": 0.9871377944946288,
            "Time in s": 15.218796
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.1314798119108302,
            "RMSE": 2.748614104980716,
            "R2": -1.180190104825623,
            "Memory in Mb": 0.955540657043457,
            "Time in s": 16.316332
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.1121913646065007,
            "RMSE": 2.708986615305391,
            "R2": -1.102550782410015,
            "Memory in Mb": 0.9793291091918944,
            "Time in s": 17.449759
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.096472283083769,
            "RMSE": 2.6715401075955145,
            "R2": -1.0771388394715324,
            "Memory in Mb": 1.0325212478637695,
            "Time in s": 18.614745
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0884657542544798,
            "RMSE": 2.639348967980305,
            "R2": -1.080631470653255,
            "Memory in Mb": 1.1148195266723633,
            "Time in s": 19.813024
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0667544669913536,
            "RMSE": 2.603003384812668,
            "R2": -1.0681837571806945,
            "Memory in Mb": 1.1698732376098633,
            "Time in s": 21.046603
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0459321867530782,
            "RMSE": 2.5682868281355016,
            "R2": -1.0121733037883445,
            "Memory in Mb": 1.2092561721801758,
            "Time in s": 22.315315
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0276781933457848,
            "RMSE": 2.5353029000371494,
            "R2": -0.9820644398878616,
            "Memory in Mb": 1.2420778274536133,
            "Time in s": 23.623046
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0094276125302497,
            "RMSE": 2.50338787783782,
            "R2": -0.9411341749539492,
            "Memory in Mb": 1.3017473220825195,
            "Time in s": 24.968597
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 1.0023537746213038,
            "RMSE": 2.475512975868657,
            "R2": -0.9153129864924484,
            "Memory in Mb": 1.3318758010864258,
            "Time in s": 26.357821
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9977235614586972,
            "RMSE": 2.450813157375169,
            "R2": -0.8978992844128302,
            "Memory in Mb": 1.3786516189575195,
            "Time in s": 27.784762
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9889333901170724,
            "RMSE": 2.4246168260512984,
            "R2": -0.8747893145143344,
            "Memory in Mb": 1.416356086730957,
            "Time in s": 29.251496
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9712423333697714,
            "RMSE": 2.3967734443047704,
            "R2": -0.8288218633529623,
            "Memory in Mb": 1.4480867385864258,
            "Time in s": 30.757563999999995
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9593965092028914,
            "RMSE": 2.3708401769846086,
            "R2": -0.7805683851951253,
            "Memory in Mb": 1.4688615798950195,
            "Time in s": 32.305297
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9500350341868696,
            "RMSE": 2.346029725301664,
            "R2": -0.7508441641708208,
            "Memory in Mb": 1.3691072463989258,
            "Time in s": 33.916341
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9362562616709212,
            "RMSE": 2.321054413049932,
            "R2": -0.7419227486050888,
            "Memory in Mb": 1.2137422561645508,
            "Time in s": 35.592854
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9293426247327622,
            "RMSE": 2.2986373047272863,
            "R2": -0.7229310397545319,
            "Memory in Mb": 1.2394838333129885,
            "Time in s": 37.31016399999999
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9223382441623138,
            "RMSE": 2.2770208564096435,
            "R2": -0.7083555493245846,
            "Memory in Mb": 1.2827730178833008,
            "Time in s": 39.06327099999999
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9155630176835056,
            "RMSE": 2.256277668055956,
            "R2": -0.7099489887647161,
            "Memory in Mb": 1.2986268997192385,
            "Time in s": 40.85878199999999
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Bagging",
            "dataset": "TrumpApproval",
            "MAE": 0.9044154317407224,
            "RMSE": 2.234829366963466,
            "R2": -0.7058332444386559,
            "Memory in Mb": 1.3350114822387695,
            "Time in s": 42.69044199999999
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 41.63636363636363,
            "RMSE": 41.64569169030137,
            "R2": -2231.5319148936137,
            "Memory in Mb": 0.0524826049804687,
            "Time in s": 0.006254
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 41.31818181818181,
            "RMSE": 41.32960638133835,
            "R2": -1808.0547045951903,
            "Memory in Mb": 0.0595359802246093,
            "Time in s": 0.016967
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 41.12121212121212,
            "RMSE": 41.13871582091424,
            "R2": -1174.393494897962,
            "Memory in Mb": 0.0739974975585937,
            "Time in s": 0.032538
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 41.159090909090914,
            "RMSE": 41.17451771534076,
            "R2": -1333.7620984139928,
            "Memory in Mb": 0.0802268981933593,
            "Time in s": 0.0535149999999999
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 41.5090909090909,
            "RMSE": 41.57075020645253,
            "R2": -336.3506066081568,
            "Memory in Mb": 0.0978660583496093,
            "Time in s": 0.0804889999999999
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 42.681818181818166,
            "RMSE": 42.82080349691271,
            "R2": -153.29834830483878,
            "Memory in Mb": 0.121429443359375,
            "Time in s": 0.1147379999999999
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 43.50649350649351,
            "RMSE": 43.70978671356627,
            "R2": -106.75487995129542,
            "Memory in Mb": 0.1384239196777343,
            "Time in s": 0.1574789999999999
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 44.21590909090909,
            "RMSE": 44.43649707984724,
            "R2": -99.97346126163,
            "Memory in Mb": 0.1540603637695312,
            "Time in s": 0.209356
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 45.05050505050505,
            "RMSE": 45.309262771858165,
            "R2": -86.8022342468144,
            "Memory in Mb": 0.1602935791015625,
            "Time in s": 0.271082
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 46.16363636363636,
            "RMSE": 46.52487115902242,
            "R2": -63.64797006437341,
            "Memory in Mb": 0.164306640625,
            "Time in s": 0.3431619999999999
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 47.21487603305785,
            "RMSE": 47.67304278378361,
            "R2": -51.27707184490422,
            "Memory in Mb": 0.1650009155273437,
            "Time in s": 0.4251659999999999
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 48.29545454545455,
            "RMSE": 48.843054157105485,
            "R2": -43.84882422437649,
            "Memory in Mb": 0.165863037109375,
            "Time in s": 0.5168919999999999
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 49.44055944055945,
            "RMSE": 50.100318941519305,
            "R2": -37.220279564063546,
            "Memory in Mb": 0.1322584152221679,
            "Time in s": 0.622087
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 50.532467532467535,
            "RMSE": 51.29137544271156,
            "R2": -33.04474826644667,
            "Memory in Mb": 0.1404676437377929,
            "Time in s": 0.736412
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 51.690909090909095,
            "RMSE": 52.61253451297311,
            "R2": -27.795548438273773,
            "Memory in Mb": 0.1464834213256836,
            "Time in s": 0.8597999999999999
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 53.00568181818182,
            "RMSE": 54.11860921749895,
            "R2": -23.566226925646237,
            "Memory in Mb": 0.1528844833374023,
            "Time in s": 0.99286
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 54.41176470588235,
            "RMSE": 55.733754017636336,
            "R2": -20.33250305682894,
            "Memory in Mb": 0.1579313278198242,
            "Time in s": 1.135584
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 56.02525252525252,
            "RMSE": 57.635786091488654,
            "R2": -17.146924852486976,
            "Memory in Mb": 0.1600141525268554,
            "Time in s": 1.287864
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 57.5645933014354,
            "RMSE": 59.46206220864915,
            "R2": -14.922837840066968,
            "Memory in Mb": 0.1255407333374023,
            "Time in s": 1.454924
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 58.69090909090908,
            "RMSE": 60.81327606250582,
            "R2": -13.581197962556498,
            "Memory in Mb": 0.1323118209838867,
            "Time in s": 1.63074
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 60.25541125541125,
            "RMSE": 62.66764529032318,
            "R2": -12.244451024360147,
            "Memory in Mb": 0.1370038986206054,
            "Time in s": 1.815352
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 62.17355371900826,
            "RMSE": 65.06963847478845,
            "R2": -10.489760184397111,
            "Memory in Mb": 0.1415891647338867,
            "Time in s": 2.009009
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 63.93675889328063,
            "RMSE": 67.17295239601157,
            "R2": -9.634560128382748,
            "Memory in Mb": 0.1452207565307617,
            "Time in s": 2.211595
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 65.10606060606062,
            "RMSE": 68.57980310513724,
            "R2": -9.127665748505592,
            "Memory in Mb": 0.1458845138549804,
            "Time in s": 2.423132
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 66.61454545454548,
            "RMSE": 70.46451073219248,
            "R2": -8.408339126213217,
            "Memory in Mb": 0.1459379196166992,
            "Time in s": 2.643805
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 68.48951048951052,
            "RMSE": 72.8020594498525,
            "R2": -7.6983532427125105,
            "Memory in Mb": 0.1282644271850586,
            "Time in s": 2.877713
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 70.55218855218858,
            "RMSE": 75.3669362796119,
            "R2": -7.08492451355157,
            "Memory in Mb": 0.1300420761108398,
            "Time in s": 3.120317
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 72.39285714285718,
            "RMSE": 77.65033596401675,
            "R2": -6.643510181414674,
            "Memory in Mb": 0.1343069076538086,
            "Time in s": 3.37158
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 73.45454545454551,
            "RMSE": 79.15086186624424,
            "R2": -6.206879640065647,
            "Memory in Mb": 0.1407041549682617,
            "Time in s": 3.631653
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 75.77878787878792,
            "RMSE": 82.20832738177494,
            "R2": -5.653192449779911,
            "Memory in Mb": 0.1449460983276367,
            "Time in s": 3.900744
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 77.92375366568919,
            "RMSE": 84.89106353805269,
            "R2": -5.352795814687307,
            "Memory in Mb": 0.1466054916381836,
            "Time in s": 4.1790140000000005
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 80.04545454545458,
            "RMSE": 87.49376601169416,
            "R2": -5.134510311668016,
            "Memory in Mb": 0.1466588973999023,
            "Time in s": 4.46626
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 80.99724517906337,
            "RMSE": 88.57562798692558,
            "R2": -5.105139086016474,
            "Memory in Mb": 0.1461553573608398,
            "Time in s": 4.762509
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 82.77807486631018,
            "RMSE": 90.83029071422122,
            "R2": -4.901675845817959,
            "Memory in Mb": 0.1569280624389648,
            "Time in s": 5.06867
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 85.1766233766234,
            "RMSE": 93.99517810235533,
            "R2": -4.591702735915359,
            "Memory in Mb": 0.1629590988159179,
            "Time in s": 5.384646
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 87.26767676767678,
            "RMSE": 96.48964983485284,
            "R2": -4.494054297851511,
            "Memory in Mb": 0.1698560714721679,
            "Time in s": 5.710516
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 89.00737100737103,
            "RMSE": 98.71879502607636,
            "R2": -4.345544683073043,
            "Memory in Mb": 0.1741170883178711,
            "Time in s": 6.048375
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 90.57416267942588,
            "RMSE": 100.72635724110243,
            "R2": -4.224084264201084,
            "Memory in Mb": 0.1756696701049804,
            "Time in s": 6.396311
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 93.12121212121215,
            "RMSE": 104.19735398794236,
            "R2": -3.967717840349581,
            "Memory in Mb": 0.1753263473510742,
            "Time in s": 6.754458
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 95.41818181818184,
            "RMSE": 107.03565676064125,
            "R2": -3.8710119659250095,
            "Memory in Mb": 0.1580381393432617,
            "Time in s": 7.124987
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 97.16629711751663,
            "RMSE": 109.07665280092142,
            "R2": -3.843505105397095,
            "Memory in Mb": 0.1671514511108398,
            "Time in s": 7.505263
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 98.71645021645024,
            "RMSE": 111.1763643167196,
            "R2": -3.72620239405422,
            "Memory in Mb": 0.1737470626831054,
            "Time in s": 7.89547
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 101.54122621564484,
            "RMSE": 115.2058457378686,
            "R2": -3.48124047566686,
            "Memory in Mb": 0.1785993576049804,
            "Time in s": 8.295795
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 103.77066115702482,
            "RMSE": 117.90601559037044,
            "R2": -3.4365483842712585,
            "Memory in Mb": 0.1823682785034179,
            "Time in s": 8.706368
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 106.02424242424244,
            "RMSE": 120.71525892518191,
            "R2": -3.37467008920777,
            "Memory in Mb": 0.1661062240600586,
            "Time in s": 9.13027
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 107.31620553359684,
            "RMSE": 122.26004165941237,
            "R2": -3.356924458603192,
            "Memory in Mb": 0.1709508895874023,
            "Time in s": 9.564033
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 109.39651837524178,
            "RMSE": 124.91233289427784,
            "R2": -3.291877964737682,
            "Memory in Mb": 0.1725950241088867,
            "Time in s": 10.007821
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 112.36553030303028,
            "RMSE": 129.1106745698386,
            "R2": -3.1225038051323804,
            "Memory in Mb": 0.1781835556030273,
            "Time in s": 10.461944
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 114.52504638218922,
            "RMSE": 131.65752925403248,
            "R2": -3.109734667916423,
            "Memory in Mb": 0.1829481124877929,
            "Time in s": 10.926196
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 115.89999999999996,
            "RMSE": 133.35909826820617,
            "R2": -3.0866973064470367,
            "Memory in Mb": 0.1825780868530273,
            "Time in s": 11.400602999999998
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 117.86452762923346,
            "RMSE": 135.8046463151548,
            "R2": -3.0526234314410727,
            "Memory in Mb": 0.1822462081909179,
            "Time in s": 11.885435
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "ChickWeights",
            "MAE": 120.54020979020974,
            "RMSE": 139.4624607986965,
            "R2": -2.953338846956928,
            "Memory in Mb": 0.1833868026733398,
            "Time in s": 12.380554
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 43.8732195,
            "RMSE": 43.87807788634269,
            "R2": -4514.954899312423,
            "Memory in Mb": 0.1279449462890625,
            "Time in s": 0.015909
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 42.4932955,
            "RMSE": 42.52255283421693,
            "R2": -725.9491167623446,
            "Memory in Mb": 0.1855659484863281,
            "Time in s": 0.053644
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 42.2167785,
            "RMSE": 42.2386240157387,
            "R2": -966.0073736019044,
            "Memory in Mb": 0.2224998474121093,
            "Time in s": 0.118601
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 41.975705625,
            "RMSE": 41.99760868559829,
            "R2": -957.9655948743646,
            "Memory in Mb": 0.2547683715820312,
            "Time in s": 0.215522
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 41.37550450000001,
            "RMSE": 41.410913785433536,
            "R2": -583.9966399141301,
            "Memory in Mb": 0.2853622436523437,
            "Time in s": 0.349036
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.936110000000006,
            "RMSE": 40.97829382197767,
            "R2": -484.9611418859003,
            "Memory in Mb": 0.2942886352539062,
            "Time in s": 0.520816
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.6885472857143,
            "RMSE": 40.72961738075088,
            "R2": -495.1050461477588,
            "Memory in Mb": 0.2989387512207031,
            "Time in s": 0.713599
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.35105437500001,
            "RMSE": 40.39801158334292,
            "R2": -429.4078677932073,
            "Memory in Mb": 0.2328748703002929,
            "Time in s": 0.934381
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.00981655555555,
            "RMSE": 40.06373388340122,
            "R2": -370.7794659133543,
            "Memory in Mb": 0.2508001327514648,
            "Time in s": 1.175315
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.80633095,
            "RMSE": 39.860362966711,
            "R2": -368.1089073295326,
            "Memory in Mb": 0.1596212387084961,
            "Time in s": 1.445583
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.727043136363626,
            "RMSE": 39.77723500009918,
            "R2": -395.5019807293188,
            "Memory in Mb": 0.1831541061401367,
            "Time in s": 1.734898
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.56323079166665,
            "RMSE": 39.61325406766278,
            "R2": -395.19837684116754,
            "Memory in Mb": 0.1905164718627929,
            "Time in s": 2.043551
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.42014538461535,
            "RMSE": 39.46968290441584,
            "R2": -397.63185900832246,
            "Memory in Mb": 0.2020750045776367,
            "Time in s": 2.371621
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.33200189285712,
            "RMSE": 39.37942345737111,
            "R2": -414.4560159350036,
            "Memory in Mb": 0.2260313034057617,
            "Time in s": 2.720012
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.18435719999999,
            "RMSE": 39.23275803924839,
            "R2": -404.5402138221895,
            "Memory in Mb": 0.2437810897827148,
            "Time in s": 3.088623
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.13568690624999,
            "RMSE": 39.1818628962716,
            "R2": -423.5167725219512,
            "Memory in Mb": 0.2581815719604492,
            "Time in s": 3.477665
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.14620944117645,
            "RMSE": 39.18989510023786,
            "R2": -447.7943063391533,
            "Memory in Mb": 0.2493734359741211,
            "Time in s": 3.892527
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.24072974999997,
            "RMSE": 39.28395553300239,
            "R2": -453.6543473793619,
            "Memory in Mb": 0.2643537521362304,
            "Time in s": 4.328145999999999
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.29597665789471,
            "RMSE": 39.33769921546023,
            "R2": -470.6701690846498,
            "Memory in Mb": 0.2747945785522461,
            "Time in s": 4.784845
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.35730624999997,
            "RMSE": 39.39781946688104,
            "R2": -485.4842825426507,
            "Memory in Mb": 0.2898855209350586,
            "Time in s": 5.262664
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.40549083333331,
            "RMSE": 39.44465897881697,
            "R2": -502.7799504226928,
            "Memory in Mb": 0.2975950241088867,
            "Time in s": 5.761624
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.49730674999998,
            "RMSE": 39.53710368662846,
            "R2": -495.9856416828035,
            "Memory in Mb": 0.3090314865112304,
            "Time in s": 6.281948
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.61474728260867,
            "RMSE": 39.65658853240579,
            "R2": -473.14358309219216,
            "Memory in Mb": 0.3255758285522461,
            "Time in s": 6.824272
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.71032456249997,
            "RMSE": 39.75304758270976,
            "R2": -464.4916761787406,
            "Memory in Mb": 0.3411321640014648,
            "Time in s": 7.389190999999999
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.80313951999997,
            "RMSE": 39.84667590965187,
            "R2": -456.8750824508669,
            "Memory in Mb": 0.2797002792358398,
            "Time in s": 7.981206999999999
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.87354713461536,
            "RMSE": 39.916931033645376,
            "R2": -459.2932847271911,
            "Memory in Mb": 0.2906713485717773,
            "Time in s": 8.594204
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.94649651851849,
            "RMSE": 39.98996046818772,
            "R2": -459.28610565666287,
            "Memory in Mb": 0.2965841293334961,
            "Time in s": 9.232432
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 39.97606614285712,
            "RMSE": 40.018487723609816,
            "R2": -470.926187706672,
            "Memory in Mb": 0.3019857406616211,
            "Time in s": 9.891908
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.00338510344825,
            "RMSE": 40.044755101652726,
            "R2": -483.2331705341176,
            "Memory in Mb": 0.3056249618530273,
            "Time in s": 10.572818
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.07393431666663,
            "RMSE": 40.11569326301364,
            "R2": -479.5746686678817,
            "Memory in Mb": 0.3106412887573242,
            "Time in s": 11.275213
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.1459417741935,
            "RMSE": 40.18827077358568,
            "R2": -473.96334667177865,
            "Memory in Mb": 0.3147268295288086,
            "Time in s": 11.999135999999998
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.21943815624997,
            "RMSE": 40.26249426545423,
            "R2": -466.8085709746123,
            "Memory in Mb": 0.3194303512573242,
            "Time in s": 12.744586999999996
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.28296777272724,
            "RMSE": 40.32626722721455,
            "R2": -464.9172853497744,
            "Memory in Mb": 0.3247060775756836,
            "Time in s": 13.511768999999996
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.31998279411761,
            "RMSE": 40.36256991107017,
            "R2": -473.1325264408024,
            "Memory in Mb": 0.3289289474487304,
            "Time in s": 14.300919999999998
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.31359012857138,
            "RMSE": 40.35509446667054,
            "R2": -485.40526703956544,
            "Memory in Mb": 0.2762861251831054,
            "Time in s": 15.116749
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.31730695833329,
            "RMSE": 40.357915759594896,
            "R2": -496.1610725544049,
            "Memory in Mb": 0.2866239547729492,
            "Time in s": 15.953537
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.36653568918915,
            "RMSE": 40.40711941642496,
            "R2": -497.0742803710164,
            "Memory in Mb": 0.2274045944213867,
            "Time in s": 16.820776
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.40314367105261,
            "RMSE": 40.443256311482514,
            "R2": -503.3712175162706,
            "Memory in Mb": 0.2380895614624023,
            "Time in s": 17.708028
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.44545064102563,
            "RMSE": 40.48534274444009,
            "R2": -506.6856716110208,
            "Memory in Mb": 0.2534551620483398,
            "Time in s": 18.615628
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.47854825,
            "RMSE": 40.518050685964006,
            "R2": -512.1052117095793,
            "Memory in Mb": 0.2672185897827148,
            "Time in s": 19.543925
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.50894034146341,
            "RMSE": 40.5479845946661,
            "R2": -518.5068774177179,
            "Memory in Mb": 0.2752447128295898,
            "Time in s": 20.493024
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.5406558690476,
            "RMSE": 40.57931089736599,
            "R2": -524.140575335229,
            "Memory in Mb": 0.2841558456420898,
            "Time in s": 21.463054
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.58371181395347,
            "RMSE": 40.62239247493601,
            "R2": -524.3496319016275,
            "Memory in Mb": 0.2900037765502929,
            "Time in s": 22.454245
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.62855514772725,
            "RMSE": 40.66738601007716,
            "R2": -522.897851512946,
            "Memory in Mb": 0.2707319259643554,
            "Time in s": 23.471721
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.664104233333326,
            "RMSE": 40.702738445808535,
            "R2": -526.020768835918,
            "Memory in Mb": 0.2802000045776367,
            "Time in s": 24.510012
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.68274704347825,
            "RMSE": 40.72073961991632,
            "R2": -535.1540147256861,
            "Memory in Mb": 0.2901716232299804,
            "Time in s": 25.569536
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.70972619148935,
            "RMSE": 40.74737437775791,
            "R2": -540.4099749760601,
            "Memory in Mb": 0.2975721359252929,
            "Time in s": 26.655616
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.73400636458332,
            "RMSE": 40.771242977826994,
            "R2": -546.7118652484228,
            "Memory in Mb": 0.3080549240112304,
            "Time in s": 27.763054
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.74031829795916,
            "RMSE": 40.77684015923968,
            "R2": -557.5026042066913,
            "Memory in Mb": 0.3134031295776367,
            "Time in s": 28.892281
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "Exponentially Weighted Average",
            "dataset": "TrumpApproval",
            "MAE": 40.75359492299998,
            "RMSE": 40.78950075300399,
            "R2": -567.2567645513548,
            "Memory in Mb": 0.3166418075561523,
            "Time in s": 30.043213999999995
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 41.63636363636363,
            "RMSE": 41.64569169030137,
            "R2": -2231.5319148936137,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.028772
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 41.31818181818181,
            "RMSE": 41.32960638133835,
            "R2": -1808.0547045951903,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.079044
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 41.12121212121212,
            "RMSE": 41.13871582091424,
            "R2": -1174.393494897962,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.149857
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 41.159090909090914,
            "RMSE": 41.17451771534076,
            "R2": -1333.7620984139928,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.237747
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 41.5090909090909,
            "RMSE": 41.57075020645253,
            "R2": -336.3506066081568,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.338425
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 42.681818181818166,
            "RMSE": 42.82080349691271,
            "R2": -153.29834830483878,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.452041
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 43.46441536424646,
            "RMSE": 43.6630525281676,
            "R2": -106.5245816691109,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.578307
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 43.36686847531974,
            "RMSE": 43.58986852756654,
            "R2": -96.16251088961316,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.71715
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 39.3777319762956,
            "RMSE": 41.29293125499619,
            "R2": -71.92610223487543,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 0.8686729999999999
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 36.38865389064824,
            "RMSE": 39.46494228501369,
            "R2": -45.51654802750055,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 1.032976
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 33.47571311046551,
            "RMSE": 37.6638192516392,
            "R2": -31.6297858502766,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 1.209623
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 30.829458151969483,
            "RMSE": 36.06523958622657,
            "R2": -23.452489437409387,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 1.398231
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 28.6940047418964,
            "RMSE": 34.66464981164902,
            "R2": -17.297279097398025,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 1.59888
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 26.901670019158168,
            "RMSE": 33.42439644535526,
            "R2": -13.457346308406352,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 1.811498
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 25.73601455188179,
            "RMSE": 32.42918896219868,
            "R2": -9.940044331027543,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 2.036514
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 24.44416894616589,
            "RMSE": 31.465121114844862,
            "R2": -7.304318935113031,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 2.273516
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 23.31106527863985,
            "RMSE": 30.560727675640003,
            "R2": -5.414053903472148,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 2.522216
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 22.2497659881735,
            "RMSE": 29.72926965926448,
            "R2": -3.828220321961205,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 2.782587
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.58385771370322,
            "RMSE": 29.10991604615937,
            "R2": -2.8161237021822814,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 3.05463
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.489125733317938,
            "RMSE": 28.89967848441583,
            "R2": -2.2929294700983545,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 3.338483
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.96077526896472,
            "RMSE": 28.36167354440183,
            "R2": -1.7127571457874735,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 3.633999
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.684837308385998,
            "RMSE": 27.97322591752617,
            "R2": -1.123436519018493,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 3.941181
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.10836609318901,
            "RMSE": 27.433189641281587,
            "R2": -0.7737126718723288,
            "Memory in Mb": 0.0121526718139648,
            "Time in s": 4.259926
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.477468707260805,
            "RMSE": 27.77140109557264,
            "R2": -0.6607814047377214,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 4.590346
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.61134029899391,
            "RMSE": 28.056502395486245,
            "R2": -0.491554549366604,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 4.932228
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.562403371381592,
            "RMSE": 27.861367163045813,
            "R2": -0.2739563786996055,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 5.285550000000001
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.2802158532438,
            "RMSE": 27.63742758295081,
            "R2": -0.0872000961905188,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 5.650314000000001
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 20.449355350398,
            "RMSE": 27.920149137510645,
            "R2": 0.0118073081415535,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 6.026518000000001
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.50134169290969,
            "RMSE": 30.009678165732637,
            "R2": -0.0359973595319296,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 6.414170000000001
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.657358056011915,
            "RMSE": 30.050226639054536,
            "R2": 0.1110159573580076,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 6.813245000000001
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.886687938329302,
            "RMSE": 30.333453058468624,
            "R2": 0.1888808568866784,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 7.223789000000001
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 21.886047000767118,
            "RMSE": 30.34044931799507,
            "R2": 0.2623171341711791,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 7.645758000000001
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 22.895757506339034,
            "RMSE": 32.0447958992957,
            "R2": 0.2009350122171253,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 8.07951
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 23.75249563906416,
            "RMSE": 33.838912051163845,
            "R2": 0.1808815149406113,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 8.524693000000001
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 24.560900349589296,
            "RMSE": 34.753482086388026,
            "R2": 0.2355843412503995,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 8.981311000000002
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 24.352453583923488,
            "RMSE": 34.473609026370774,
            "R2": 0.2986981406442135,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 9.449373
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 25.719275464870663,
            "RMSE": 37.04357441923364,
            "R2": 0.2473067090757558,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 9.928858000000002
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 27.096550121003176,
            "RMSE": 39.902565812758986,
            "R2": 0.1801666848023049,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 10.419752000000004
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 28.343681876579897,
            "RMSE": 42.0624752869508,
            "R2": 0.1904695440990398,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 10.922067000000002
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 29.341897763641,
            "RMSE": 43.65194027092424,
            "R2": 0.1898427093039769,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 11.435807000000002
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 30.67273802938304,
            "RMSE": 45.6370688200433,
            "R2": 0.1521253661768283,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 11.960959000000004
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 32.56224145473062,
            "RMSE": 49.915337115223885,
            "R2": 0.0473016837570096,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 12.497734000000005
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 34.43415680949522,
            "RMSE": 53.78695495416363,
            "R2": 0.0232056621878617,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 13.045956000000004
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 37.59302308486845,
            "RMSE": 59.43178585545712,
            "R2": -0.1272256336981969,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 13.605608000000004
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 39.81029832190851,
            "RMSE": 63.2563754686467,
            "R2": -0.2012394142017446,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 14.176690000000004
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 40.81849028215024,
            "RMSE": 64.7117163856453,
            "R2": -0.2206096222811289,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 14.759208000000005
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 42.30053541895924,
            "RMSE": 66.69347450894223,
            "R2": -0.2234984190364006,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 15.353157000000005
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 43.87998520264807,
            "RMSE": 69.22658128427689,
            "R2": -0.1851751428384946,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 15.958328000000003
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 45.090482136166365,
            "RMSE": 70.91807128614899,
            "R2": -0.1924391171188431,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 16.574693000000003
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 46.16603381063717,
            "RMSE": 72.79977252028388,
            "R2": -0.2178315347358042,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 17.202244000000004
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 47.99895001321041,
            "RMSE": 75.49864048778444,
            "R2": -0.2525216922711382,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 17.841166000000005
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "ChickWeights",
            "MAE": 49.57826542612398,
            "RMSE": 77.90262570405233,
            "R2": -0.2335409846027114,
            "Memory in Mb": 0.012312889099121,
            "Time in s": 18.491295000000004
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 30.45103241731707,
            "RMSE": 33.23585723529438,
            "R2": -2590.0045530336465,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.03648
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 18.3406114455606,
            "RMSE": 24.1628558112126,
            "R2": -233.72636807636488,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.100456
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 14.012302795940927,
            "RMSE": 20.27429916426714,
            "R2": -221.7932161673039,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.190991
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 11.49107264681655,
            "RMSE": 17.720640796103456,
            "R2": -169.73114207921216,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.307239
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 9.726608796116103,
            "RMSE": 15.913172800750536,
            "R2": -85.38479390162912,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.4491740000000001
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 8.642897473622819,
            "RMSE": 14.610205599232696,
            "R2": -60.77410396737057,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.6162740000000001
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 7.627861449957184,
            "RMSE": 13.547130531753504,
            "R2": -53.88423494401591,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 0.8076440000000001
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 6.825616478903957,
            "RMSE": 12.68640242718137,
            "R2": -41.44604107616888,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 1.023068
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 6.298325880816026,
            "RMSE": 11.99455373608459,
            "R2": -32.32351025206219,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 1.262663
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 5.791221405645649,
            "RMSE": 11.389261045241726,
            "R2": -29.134439780883504,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 1.526002
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 5.429217208457164,
            "RMSE": 10.877504011291329,
            "R2": -28.650681734644422,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 1.812923
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 5.060396678997669,
            "RMSE": 10.421476408956162,
            "R2": -26.4214333861576,
            "Memory in Mb": 0.0131101608276367,
            "Time in s": 2.123256
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 4.7577579662422185,
            "RMSE": 10.01970369652003,
            "R2": -24.68943115642662,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 2.456738
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 4.47898479527949,
            "RMSE": 9.659781964354623,
            "R2": -23.99890538466576,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 2.813161
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 4.231628573868652,
            "RMSE": 9.33546881214548,
            "R2": -21.961936464609707,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 3.192823
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 4.032288217093912,
            "RMSE": 9.046394584789834,
            "R2": -21.629541054113563,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 3.5954460000000004
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.8351551756309497,
            "RMSE": 8.779241117397504,
            "R2": -21.522318216666985,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 4.021045
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.660607443401045,
            "RMSE": 8.536652519215579,
            "R2": -20.469707840891584,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 4.469678
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.505270605120577,
            "RMSE": 8.311598150636895,
            "R2": -20.056664379019765,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 4.941134
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.360453882251005,
            "RMSE": 8.10307441673556,
            "R2": -19.578991923208985,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 5.435716
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.230603986740656,
            "RMSE": 7.909485894846834,
            "R2": -19.256340082684435,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 5.953156
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.1198347345540465,
            "RMSE": 7.731010347257149,
            "R2": -18.002320884204543,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 6.493473
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 3.010353198494384,
            "RMSE": 7.562877110682495,
            "R2": -16.244605442867506,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 7.056611999999999
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.9023580604284582,
            "RMSE": 7.404341650720478,
            "R2": -15.148937801753288,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 7.642589999999999
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.8120368518109427,
            "RMSE": 7.256642134427339,
            "R2": -14.185679409391112,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 8.251631
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.722217494708863,
            "RMSE": 7.11705765703134,
            "R2": -13.632593906904136,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 8.883484
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.6379600337769933,
            "RMSE": 6.984812005374008,
            "R2": -13.042206620144157,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 9.537691
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.573532085936036,
            "RMSE": 6.862931118690264,
            "R2": -12.879442173523902,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 10.214296
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.508294944253365,
            "RMSE": 6.745457437445754,
            "R2": -12.739978855164816,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 10.913296
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.4431260057234407,
            "RMSE": 6.633435680824833,
            "R2": -12.140422111767563,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 11.634954
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.386700775516181,
            "RMSE": 6.528113194197335,
            "R2": -11.53247390884172,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 12.379039999999998
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.3242014075410804,
            "RMSE": 6.426013651213371,
            "R2": -10.916538218303476,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 13.145560999999995
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.2685968162113417,
            "RMSE": 6.328883008296775,
            "R2": -10.475904112331508,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 13.934486999999995
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.2077966601853354,
            "RMSE": 6.235306598260896,
            "R2": -10.31508330333358,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 14.745848999999998
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.1581493026656715,
            "RMSE": 6.146460408814674,
            "R2": -10.283704638807178,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 15.579853999999996
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.1027567473920863,
            "RMSE": 6.060643545524585,
            "R2": -10.211846444382044,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 16.436290999999997
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.051121816682194,
            "RMSE": 5.978350933609188,
            "R2": -9.90287777753909,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 17.315177999999996
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 2.003155134641025,
            "RMSE": 5.899358540561457,
            "R2": -9.731678337792127,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 18.216514
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.9581628436412764,
            "RMSE": 5.823548668044576,
            "R2": -9.504483044737295,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 19.140319
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.920522972774301,
            "RMSE": 5.751090425279772,
            "R2": -9.337362153707344,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 20.086783
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.884378546616626,
            "RMSE": 5.681435320930898,
            "R2": -9.199265318679966,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 21.055682
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.8462172344878476,
            "RMSE": 5.613649762186833,
            "R2": -9.049787223051387,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 22.047027
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.8114873001009923,
            "RMSE": 5.548504609880171,
            "R2": -8.800976301633217,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 23.060786
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.7737427907909609,
            "RMSE": 5.485176730961097,
            "R2": -8.530931568707373,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 24.096958
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.7378742216236305,
            "RMSE": 5.423968591721732,
            "R2": -8.358684442608821,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 25.155795
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.7058202733924563,
            "RMSE": 5.364926267836746,
            "R2": -8.30648673172487,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 26.237104
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.6771033983092818,
            "RMSE": 5.307938337650396,
            "R2": -8.187106100071555,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 27.340904
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.6470899020587193,
            "RMSE": 5.252615019014566,
            "R2": -8.09065943244505,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 28.467203
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.6179664800066769,
            "RMSE": 5.198922142498095,
            "R2": -8.078721464420347,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 29.615952
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "River MLP",
            "dataset": "TrumpApproval",
            "MAE": 1.591389315944533,
            "RMSE": 5.1470018023734205,
            "R2": -8.048080908594342,
            "Memory in Mb": 0.013350486755371,
            "Time in s": 30.787287
          },
          {
            "step": 11,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 4.664574314574316,
            "RMSE": 12.7079745317607,
            "R2": -206.87879383707747,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.002154
          },
          {
            "step": 22,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 2.767694704637076,
            "RMSE": 9.018587183866767,
            "R2": -85.14025986830408,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.005944
          },
          {
            "step": 33,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 2.3093367298127023,
            "RMSE": 7.420500566500976,
            "R2": -37.24267181629702,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.010037
          },
          {
            "step": 44,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 1.892363968348808,
            "RMSE": 6.441521936619904,
            "R2": -31.668094594906044,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.014469
          },
          {
            "step": 55,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 2.1129412159858934,
            "RMSE": 6.114058653243701,
            "R2": -6.297346571779499,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.019181
          },
          {
            "step": 66,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 2.832849782567835,
            "RMSE": 6.236602142425367,
            "R2": -2.2730130120415795,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.024182
          },
          {
            "step": 77,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 3.4069290990236856,
            "RMSE": 6.402381882180361,
            "R2": -1.3118663438824,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.029453
          },
          {
            "step": 88,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 3.650377971160808,
            "RMSE": 6.321189272940957,
            "R2": -1.043267371916866,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.034986
          },
          {
            "step": 99,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 4.035631404360372,
            "RMSE": 6.4483291916176695,
            "R2": -0.7783857772357967,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.040781
          },
          {
            "step": 110,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 4.693189868957898,
            "RMSE": 7.0697740144659305,
            "R2": -0.4927792786841307,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.046845
          },
          {
            "step": 121,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 5.274396860168236,
            "RMSE": 7.6542276724395,
            "R2": -0.3476225254437259,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.053171
          },
          {
            "step": 132,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 5.875758254207378,
            "RMSE": 8.194624755054596,
            "R2": -0.2624191661321591,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.05976
          },
          {
            "step": 143,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 6.530760796045927,
            "RMSE": 8.870097879563003,
            "R2": -0.1980355424044948,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.066612
          },
          {
            "step": 154,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 7.121466111912466,
            "RMSE": 9.458403141043558,
            "R2": -0.1577027852151795,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.073726
          },
          {
            "step": 165,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 7.772438504082036,
            "RMSE": 10.375670403553157,
            "R2": -0.1198999930450892,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.081109
          },
          {
            "step": 176,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 8.565827130563894,
            "RMSE": 11.410434180005833,
            "R2": -0.0920676568626532,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.088752
          },
          {
            "step": 187,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 9.429958588641576,
            "RMSE": 12.495061319237752,
            "R2": -0.0722153171628203,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.096665
          },
          {
            "step": 198,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 10.47731537859646,
            "RMSE": 13.900491647656429,
            "R2": -0.0555502703757588,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.104851
          },
          {
            "step": 209,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 11.43172675762076,
            "RMSE": 15.229123619635446,
            "R2": -0.0444565128716372,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.1133
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 11.97432098008114,
            "RMSE": 16.22368260926648,
            "R2": -0.0377560869847111,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.122025
          },
          {
            "step": 231,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 12.9382196746461,
            "RMSE": 17.489503190785292,
            "R2": -0.0315781972827118,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.131017
          },
          {
            "step": 242,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 14.229204186206864,
            "RMSE": 19.43725798629848,
            "R2": -0.0252367718674193,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.140272
          },
          {
            "step": 253,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 15.339413196393396,
            "RMSE": 20.82023831254592,
            "R2": -0.0216497893038387,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.149788
          },
          {
            "step": 264,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 15.948617107030818,
            "RMSE": 21.75817315507082,
            "R2": -0.0194401851240946,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.159572
          },
          {
            "step": 275,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 16.794155127707494,
            "RMSE": 23.16724301729152,
            "R2": -0.0169996193237813,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.169617
          },
          {
            "step": 286,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 17.990009992534457,
            "RMSE": 24.865985915258104,
            "R2": -0.0147547133955299,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.17992
          },
          {
            "step": 297,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 19.34919450213405,
            "RMSE": 26.67620929760368,
            "R2": -0.0128904565600072,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.190491
          },
          {
            "step": 308,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 20.46881241431745,
            "RMSE": 28.248013022827838,
            "R2": -0.011537481517321,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.201321
          },
          {
            "step": 319,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 20.993702124162965,
            "RMSE": 29.63814114349949,
            "R2": -0.0105036731193923,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.212414
          },
          {
            "step": 330,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 22.586872779548436,
            "RMSE": 32.01796640002603,
            "R2": -0.0092202379520505,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.223765
          },
          {
            "step": 341,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 23.97345887210737,
            "RMSE": 33.821533603903084,
            "R2": -0.0083877019037323,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.235368
          },
          {
            "step": 352,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 25.315991788770976,
            "RMSE": 35.461698606860665,
            "R2": -0.0077313021586467,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.247225
          },
          {
            "step": 363,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 25.615062978866305,
            "RMSE": 35.981300981590465,
            "R2": -0.0074437490312051,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.259337
          },
          {
            "step": 374,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 26.673321526932543,
            "RMSE": 37.51836715700961,
            "R2": -0.0069358461242559,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.271713
          },
          {
            "step": 385,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 28.27694482780972,
            "RMSE": 39.8753298933956,
            "R2": -0.0063325109838794,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.2843549999999999
          },
          {
            "step": 396,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 29.55612496209691,
            "RMSE": 41.28848705945016,
            "R2": -0.0059801818919071,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.2972059999999999
          },
          {
            "step": 407,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 30.56167711268285,
            "RMSE": 42.81802042618151,
            "R2": -0.0056467231500465,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3102509999999999
          },
          {
            "step": 418,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 31.39346669137945,
            "RMSE": 44.18765357092498,
            "R2": -0.0053697143301307,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3234889999999999
          },
          {
            "step": 429,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 33.10612890637694,
            "RMSE": 46.865579751152914,
            "R2": -0.0049663660706051,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3369199999999999
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 34.54914638861108,
            "RMSE": 48.61167278858254,
            "R2": -0.0047161238549726,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3505489999999999
          },
          {
            "step": 451,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 35.43263419295921,
            "RMSE": 49.67507127970072,
            "R2": -0.0045536938071879,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3643729999999999
          },
          {
            "step": 462,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 36.308550382896186,
            "RMSE": 51.2507761435036,
            "R2": -0.0043573774895468,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3783909999999999
          },
          {
            "step": 473,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 38.26330298063241,
            "RMSE": 54.53225049728104,
            "R2": -0.0040516612048955,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.3926029999999999
          },
          {
            "step": 484,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 39.59866234800828,
            "RMSE": 56.08659790201894,
            "R2": -0.0039023944795495,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4070059999999999
          },
          {
            "step": 495,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 40.94697327298068,
            "RMSE": 57.823326559810994,
            "R2": -0.0037535911132069,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4215999999999999
          },
          {
            "step": 506,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 41.42384714758024,
            "RMSE": 58.67984594201592,
            "R2": -0.0036652347211194,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4363849999999999
          },
          {
            "step": 517,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 42.72663002099646,
            "RMSE": 60.40151056768402,
            "R2": -0.0035345422299792,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4513639999999999
          },
          {
            "step": 528,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 44.77321528369677,
            "RMSE": 63.69509749878913,
            "R2": -0.0033415055563215,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4665329999999999
          },
          {
            "step": 539,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 45.99579764939489,
            "RMSE": 65.0494992510053,
            "R2": -0.003252609562637,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4818929999999999
          },
          {
            "step": 550,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 46.57020777663759,
            "RMSE": 66.07332710234044,
            "R2": -0.0031815200825582,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.4974459999999999
          },
          {
            "step": 561,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 47.75825760640621,
            "RMSE": 67.5643396193493,
            "R2": -0.0030950009187136,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.5131919999999999
          },
          {
            "step": 572,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "ChickWeights",
            "MAE": 49.49138874897682,
            "RMSE": 70.24569214117749,
            "R2": -0.0029719424061886,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.5291269999999999
          },
          {
            "step": 20,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 2.695184981652336,
            "RMSE": 9.807184976514188,
            "R2": -224.6021011118197,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.003379
          },
          {
            "step": 40,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 2.3994713447037435,
            "RMSE": 7.102066178895935,
            "R2": -19.27845129783118,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0081789999999999
          },
          {
            "step": 60,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.8170744682035584,
            "RMSE": 5.815253847056423,
            "R2": -17.329373299766118,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0135909999999999
          },
          {
            "step": 80,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.604995404573344,
            "RMSE": 5.081770494168446,
            "R2": -13.040545957103586,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0195849999999999
          },
          {
            "step": 100,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.824259078948539,
            "RMSE": 4.70488333223354,
            "R2": -6.5512954222403845,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0262549999999999
          },
          {
            "step": 120,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.918744608116588,
            "RMSE": 4.412336880489357,
            "R2": -4.634185300646759,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.033502
          },
          {
            "step": 140,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.8761207739327503,
            "RMSE": 4.13187920011476,
            "R2": -4.105616799680584,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.041316
          },
          {
            "step": 160,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.961232939518506,
            "RMSE": 3.976173487274506,
            "R2": -3.1695661963674864,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0496949999999999
          },
          {
            "step": 180,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 2.066134597500757,
            "RMSE": 3.873731518767916,
            "R2": -2.4756944369169624,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0586379999999999
          },
          {
            "step": 200,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 2.051125997923389,
            "RMSE": 3.731810291394655,
            "R2": -2.23527456693896,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.0682329999999999
          },
          {
            "step": 220,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.94095193468414,
            "RMSE": 3.56902990398404,
            "R2": -2.19210047340805,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.078397
          },
          {
            "step": 240,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.9366756524315063,
            "RMSE": 3.4612902974772624,
            "R2": -2.024876884626847,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.089124
          },
          {
            "step": 260,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.9250039777458068,
            "RMSE": 3.363327951159923,
            "R2": -1.8945640461454525,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.1004139999999999
          },
          {
            "step": 280,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.8726934920539136,
            "RMSE": 3.257010428159885,
            "R2": -1.8420037280027224,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.11227
          },
          {
            "step": 300,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.8907476896224935,
            "RMSE": 3.1958821895815714,
            "R2": -1.6910252267675163,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.124747
          },
          {
            "step": 320,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.819623890420079,
            "RMSE": 3.103812605138666,
            "R2": -1.663886258690169,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.137792
          },
          {
            "step": 340,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7396293145937214,
            "RMSE": 3.014220627768389,
            "R2": -1.654906383755708,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.151284
          },
          {
            "step": 360,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7350691203787965,
            "RMSE": 2.9569384317632506,
            "R2": -1.5759385016835008,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.165202
          },
          {
            "step": 380,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6987131960417108,
            "RMSE": 2.8893997308323693,
            "R2": -1.5446951110541192,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.179547
          },
          {
            "step": 400,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.673610627740774,
            "RMSE": 2.82935583501861,
            "R2": -1.5089937655143242,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.194363
          },
          {
            "step": 420,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6410137122925974,
            "RMSE": 2.7701802079251965,
            "R2": -1.484737486096575,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.209602
          },
          {
            "step": 440,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6565972573555454,
            "RMSE": 2.7427790467379385,
            "R2": -1.391750010744973,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.225268
          },
          {
            "step": 460,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.699464840115161,
            "RMSE": 2.73946740401384,
            "R2": -1.2626191030939884,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.241356
          },
          {
            "step": 480,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7224824441896145,
            "RMSE": 2.7219018737730583,
            "R2": -1.182307732575659,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.257864
          },
          {
            "step": 500,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7446092142173422,
            "RMSE": 2.70580354422956,
            "R2": -1.1113262021905803,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.274789
          },
          {
            "step": 520,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7464998751860934,
            "RMSE": 2.677192702589883,
            "R2": -1.0705208906620065,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.292197
          },
          {
            "step": 540,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7535492786865423,
            "RMSE": 2.653885630983747,
            "R2": -1.027170706279252,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.310025
          },
          {
            "step": 560,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7201019899937544,
            "RMSE": 2.614359234374483,
            "R2": -1.0141103337708768,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.328271
          },
          {
            "step": 580,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6887559504032663,
            "RMSE": 2.5757257291728384,
            "R2": -1.0033760803823184,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.346933
          },
          {
            "step": 600,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.701917368353294,
            "RMSE": 2.561424763732869,
            "R2": -0.9592753712060648,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.366058
          },
          {
            "step": 620,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7178157166185173,
            "RMSE": 2.551346895968156,
            "R2": -0.9142580419512064,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.38561
          },
          {
            "step": 640,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7365901196485038,
            "RMSE": 2.545046385321895,
            "R2": -0.8692105635365064,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.405582
          },
          {
            "step": 660,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.7465677425181807,
            "RMSE": 2.532051562790666,
            "R2": -0.8368676529707118,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.425968
          },
          {
            "step": 680,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.731617734826669,
            "RMSE": 2.504226186170861,
            "R2": -0.8251107974736909,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.446783
          },
          {
            "step": 700,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6973720107412231,
            "RMSE": 2.47026789197972,
            "R2": -0.8225927549994396,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.468073
          },
          {
            "step": 720,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6698372433333928,
            "RMSE": 2.4400355004771077,
            "R2": -0.81732226470892,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.489788
          },
          {
            "step": 740,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6732482399922957,
            "RMSE": 2.425592833263792,
            "R2": -0.7947920429290933,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.511921
          },
          {
            "step": 760,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6653913599894004,
            "RMSE": 2.404136439714782,
            "R2": -0.7822814452716051,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.53447
          },
          {
            "step": 780,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6644612180457288,
            "RMSE": 2.387561393188575,
            "R2": -0.7656652158374817,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.557436
          },
          {
            "step": 800,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6556359332933146,
            "RMSE": 2.368497267913513,
            "R2": -0.7532954885990883,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.580851
          },
          {
            "step": 820,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6452077788467467,
            "RMSE": 2.348678653798561,
            "R2": -0.7430103139622937,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.604682
          },
          {
            "step": 840,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6374623223784903,
            "RMSE": 2.3305035344735936,
            "R2": -0.7320713255917544,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.6289220000000001
          },
          {
            "step": 860,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6419505315856449,
            "RMSE": 2.320208013716276,
            "R2": -0.7138439732116804,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.653572
          },
          {
            "step": 880,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6490002164922652,
            "RMSE": 2.3126155324510744,
            "R2": -0.6941855677649247,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.6786340000000001
          },
          {
            "step": 900,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6474991175923384,
            "RMSE": 2.299197536504521,
            "R2": -0.6816400531907807,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.704114
          },
          {
            "step": 920,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6301006788336792,
            "RMSE": 2.2779225390149764,
            "R2": -0.6777843948800273,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.730046
          },
          {
            "step": 940,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6221876471839871,
            "RMSE": 2.262378737250057,
            "R2": -0.6690049120995847,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.7563869999999999
          },
          {
            "step": 960,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.6124120493571743,
            "RMSE": 2.245866476718547,
            "R2": -0.6619276404267609,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.7831509999999999
          },
          {
            "step": 980,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.5867001120604314,
            "RMSE": 2.223758235975506,
            "R2": -0.661013659831075,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.810322
          },
          {
            "step": 1000,
            "track": "Regression",
            "model": "[baseline] Mean predictor",
            "dataset": "TrumpApproval",
            "MAE": 1.5681359363812415,
            "RMSE": 2.2037391763141216,
            "R2": -0.6587014308970958,
            "Memory in Mb": 0.0004901885986328,
            "Time in s": 0.8379
          }
        ]
      },
      "params": [
        {
          "name": "models",
          "select": {
            "type": "point",
            "fields": [
              "model"
            ]
          },
          "bind": "legend"
        },
        {
          "name": "Dataset",
          "value": "ChickWeights",
          "bind": {
            "input": "select",
            "options": [
              "ChickWeights",
              "TrumpApproval"
            ]
          }
        },
        {
          "name": "grid",
          "select": "interval",
          "bind": "scales"
        }
      ],
      "transform": [
        {
          "filter": {
            "field": "dataset",
            "equal": {
              "expr": "Dataset"
            }
          }
        }
      ],
      "repeat": {
        "row": [
          "MAE",
          "RMSE",
          "R2",
          "Memory in Mb",
          "Time in s"
        ]
      },
      "spec": {
        "width": "container",
        "mark": "line",
        "encoding": {
          "x": {
            "field": "step",
            "type": "quantitative",
            "axis": {
              "titleFontSize": 18,
              "labelFontSize": 18,
              "title": "Instance"
            }
          },
          "y": {
            "field": {
              "repeat": "row"
            },
            "type": "quantitative",
            "axis": {
              "titleFontSize": 18,
              "labelFontSize": 18
            }
          },
          "color": {
            "field": "model",
            "type": "ordinal",
            "scale": {
              "scheme": "category20b"
            },
            "title": "Models",
            "legend": {
              "titleFontSize": 18,
              "labelFontSize": 18,
              "labelLimit": 500
            }
          },
          "opacity": {
            "condition": {
              "param": "models",
              "value": 1
            },
            "value": 0.2
          }
        }
      }
    }
    ```

            

## Datasets

???- abstract "ChickWeights"

    Chick weights along time.

    The stream contains 578 items and 3 features. The goal is to predict the weight of each chick
    along time, according to the diet the chick is on. The data is ordered by time and then by
    chick.

        Name  ChickWeights                                                 
        Task  Regression                                                   
     Samples  578                                                          
    Features  3                                                            
      Sparse  False                                                        
        Path  /home/kulbach/projects/river/river/datasets/chick-weights.csv

<span />

???- abstract "TrumpApproval"

    Donald Trump approval ratings.

    This dataset was obtained by reshaping the data used by FiveThirtyEight for analyzing Donald
    Trump's approval ratings. It contains 5 features, which are approval ratings collected by
    5 polling agencies. The target is the approval rating from FiveThirtyEight's model. The goal of
    this task is to see if we can reproduce FiveThirtyEight's model.

        Name  TrumpApproval                                                    
        Task  Regression                                                       
     Samples  1,001                                                            
    Features  6                                                                
      Sparse  False                                                            
        Path  /home/kulbach/projects/river/river/datasets/trump_approval.csv.gz

<span />

## Models

???- example "Linear Regression"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      LinearRegression (
        optimizer=SGD (
          lr=Constant (
            learning_rate=0.01
          )
        )
        loss=Squared ()
        l2=0.
        l1=0.
        intercept_init=0.
        intercept_lr=Constant (
          learning_rate=0.01
        )
        clip_gradient=1e+12
        initializer=Zeros ()
      )
    )</pre>

<span />

???- example "Linear Regression with l1 regularization"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      LinearRegression (
        optimizer=SGD (
          lr=Constant (
            learning_rate=0.01
          )
        )
        loss=Squared ()
        l2=0.
        l1=1.
        intercept_init=0.
        intercept_lr=Constant (
          learning_rate=0.01
        )
        clip_gradient=1e+12
        initializer=Zeros ()
      )
    )</pre>

<span />

???- example "Linear Regression with l2 regularization"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      LinearRegression (
        optimizer=SGD (
          lr=Constant (
            learning_rate=0.01
          )
        )
        loss=Squared ()
        l2=1.
        l1=0.
        intercept_init=0.
        intercept_lr=Constant (
          learning_rate=0.01
        )
        clip_gradient=1e+12
        initializer=Zeros ()
      )
    )</pre>

<span />

???- example "Passive-Aggressive Regressor, mode 1"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      PARegressor (
        C=1.
        mode=1
        eps=0.1
        learn_intercept=True
      )
    )</pre>

<span />

???- example "Passive-Aggressive Regressor, mode 2"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      PARegressor (
        C=1.
        mode=2
        eps=0.1
        learn_intercept=True
      )
    )</pre>

<span />

???- example "k-Nearest Neighbors"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      KNNRegressor (
        n_neighbors=5
        window_size=100
        aggregation_method="mean"
        min_distance_keep=0.
        distance_func=functools.partial(<function minkowski_distance at 0x7f2d38a59ea0>, p=2)
      )
    )</pre>

<span />

???- example "Hoeffding Tree"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      HoeffdingTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
      )
    )</pre>

<span />

???- example "Hoeffding Adaptive Tree"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=True
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=42
      )
    )</pre>

<span />

???- example "Stochastic Gradient Tree"

    <pre>SGTRegressor (
      delta=1e-07
      grace_period=200
      init_pred=0.
      max_depth=inf
      lambda_value=0.1
      gamma=1.
      nominal_attributes=[]
      feature_quantizer=StaticQuantizer (
        n_bins=64
        warm_start=100
        buckets=None
      )
    )</pre>

<span />

???- example "Adaptive Random Forest"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      []
    )</pre>

<span />

???- example "Adaptive Model Rules"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      AMRules (
        n_min=200
        delta=1e-07
        tau=0.05
        pred_type="adaptive"
        pred_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        splitter=TEBSTSplitter (
          digits=1
        )
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        fading_factor=0.99
        anomaly_threshold=-0.75
        m_min=30
        ordered_rule_set=True
        min_samples_split=5
      )
    )</pre>

<span />

???- example "Streaming Random Patches"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      SRPRegressor (
        model=HoeffdingTreeRegressor (
          grace_period=50
          max_depth=inf
          delta=0.01
          tau=0.05
          leaf_prediction="adaptive"
          leaf_model=LinearRegression (
            optimizer=SGD (
              lr=Constant (
                learning_rate=0.01
              )
            )
            loss=Squared ()
            l2=0.
            l1=0.
            intercept_init=0.
            intercept_lr=Constant (
              learning_rate=0.01
            )
            clip_gradient=1e+12
            initializer=Zeros ()
          )
          model_selector_decay=0.95
          nominal_attributes=None
          splitter=TEBSTSplitter (
            digits=1
          )
          min_samples_split=5
          binary_split=False
          max_size=500.
          memory_estimate_period=1000000
          stop_mem_management=False
          remove_poor_attrs=False
          merit_preprune=True
        )
        n_models=10
        subspace_size=0.6
        training_method="patches"
        lam=6
        drift_detector=ADWIN (
          delta=1e-05
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        warning_detector=ADWIN (
          delta=0.0001
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        disable_detector="off"
        disable_weighted_vote=True
        drift_detection_criteria="error"
        aggregation_method="mean"
        seed=42
        metric=MAE ()
      )
    )</pre>

<span />

???- example "Bagging"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      [HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=False
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      )]
    )</pre>

<span />

???- example "Exponentially Weighted Average"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      [LinearRegression (
        optimizer=SGD (
          lr=Constant (
            learning_rate=0.01
          )
        )
        loss=Squared ()
        l2=0.
        l1=0.
        intercept_init=0.
        intercept_lr=Constant (
          learning_rate=0.01
        )
        clip_gradient=1e+12
        initializer=Zeros ()
      ), HoeffdingAdaptiveTreeRegressor (
        grace_period=200
        max_depth=inf
        delta=1e-07
        tau=0.05
        leaf_prediction="adaptive"
        leaf_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        model_selector_decay=0.95
        nominal_attributes=None
        splitter=TEBSTSplitter (
          digits=1
        )
        min_samples_split=5
        bootstrap_sampling=True
        drift_window_threshold=300
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        switch_significance=0.05
        binary_split=False
        max_size=500.
        memory_estimate_period=1000000
        stop_mem_management=False
        remove_poor_attrs=False
        merit_preprune=True
        seed=None
      ), KNNRegressor (
        n_neighbors=5
        window_size=100
        aggregation_method="mean"
        min_distance_keep=0.
        distance_func=functools.partial(<function minkowski_distance at 0x7f2d38a59ea0>, p=2)
      ), AMRules (
        n_min=200
        delta=1e-07
        tau=0.05
        pred_type="adaptive"
        pred_model=LinearRegression (
          optimizer=SGD (
            lr=Constant (
              learning_rate=0.01
            )
          )
          loss=Squared ()
          l2=0.
          l1=0.
          intercept_init=0.
          intercept_lr=Constant (
            learning_rate=0.01
          )
          clip_gradient=1e+12
          initializer=Zeros ()
        )
        splitter=TEBSTSplitter (
          digits=1
        )
        drift_detector=ADWIN (
          delta=0.002
          clock=32
          max_buckets=5
          min_window_length=5
          grace_period=10
        )
        fading_factor=0.99
        anomaly_threshold=-0.75
        m_min=30
        ordered_rule_set=True
        min_samples_split=5
      )]
    )</pre>

<span />

???- example "River MLP"

    <pre>Pipeline (
      StandardScaler (
        with_std=True
      ),
      MLPRegressor (
        hidden_dims=(5,)
        activations=(<class 'river.neural_net.activations.ReLU'>, <class 'river.neural_net.activations.ReLU'>, <class 'river.neural_net.activations.Identity'>)
        loss=Squared ()
        optimizer=SGD (
          lr=Constant (
            learning_rate=0.001
          )
        )
        seed=42
      )
    )</pre>

<span />

???- example "[baseline] Mean predictor"

    <pre>StatisticRegressor (
      statistic=Mean ()
    )</pre>

<span />

## Environment

<pre>Python implementation: CPython
Python version       : 3.10.8
IPython version      : 8.12.0

river       : 0.15.0
numpy       : 1.24.2
scikit-learn: 1.2.2
pandas      : 1.5.3
scipy       : 1.10.1

Compiler    : Clang 14.0.0 (clang-1400.0.29.102)
OS          : Darwin
Release     : 22.2.0
Machine     : arm64
Processor   : arm
CPU cores   : 8
Architecture: 64bit
</pre>

