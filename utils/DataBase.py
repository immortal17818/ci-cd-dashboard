import connection
import pandas as pd 
df = pd.read_csv("../train.csv")
df= df.fillna(0)
column = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',     
       'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
       'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',    
       'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',    
       'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',       
       'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
       'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',    
       'HeatingQC', 'CentralAir', 'Electrical', 'SalePrice']
print(len(column))
df = df[column]

def create_database():
    cur, _ = connection.connection()
    cur.execute("CREATE DATABASE Plotly")
    return True

# def create_table():
#     cur, _ = connection.connection('Plotly')
#     cur.execute("CREATE TABLE GraphData (Id INT AUTO_INCREMENT PRIMARY KEY,\
#          {} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
#         ,{} varchar(25),{} varchar(25),{} varchar(25)\
#                                 )".format('MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 
#                                 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
#                                 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',    
#                                 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
#                                 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',    
#                                 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',       
#                                 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
#                                 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',    
#                                 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',        
#                                 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
#                                 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
#                                 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
#                                 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
#                                 'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
#                                 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
#                                 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
#                                 'SaleCondition', 'SalePrice')
#                                 )
#     return True

# def insertTable():
#     cur, conn = connection.connection('Plotly')
#     for i,row in df.iterrows():
#         sql = "INSERT INTO Plotly.GraphData (MSSubClass, MSZoning, LotFrontage, LotArea, Street,\
#             Alley, LotShape, LandContour, Utilities, LotConfig,LandSlope, Neighborhood, Condition1,\
#             Condition2, BldgType,HouseStyle,OverallQual, OverallCond,YearBuilt,YearRemodAdd,\
#             RoofStyle, RoofMatl, Exterior1st,Exterior2nd, MasVnrType,MasVnrArea, ExterQual, ExterCond,\
#             Foundation, BsmtQual,BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinSF1,BsmtFinType2, BsmtFinSF2,BsmtUnfSF,\
#             TotalBsmtSF, Heating,HeatingQC, CentralAir, Electrical, 1stFlrSF, 2ndFlrSF,LowQualFinSF, GrLivArea,\
#             BsmtFullBath, BsmtHalfBath, FullBath,HalfBath, BedroomAbvGr, KitchenAbvGr, KitchenQual,TotRmsAbvGrd,\
#             Functional, Fireplaces, FireplaceQu, GarageType,GarageYrBlt, GarageFinish, GarageCars, GarageArea, GarageQual,\
#             GarageCond, PavedDrive, WoodDeckSF, OpenPorchSF,EnclosedPorch, 3SsnPorch, ScreenPorch, PoolArea, PoolQC,\
#             Fence, MiscFeature, MiscVal, MoSold, YrSold, SaleType,SaleCondition, SalePrice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
#             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
#             %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         cur.execute(sql, tuple(row))
#         print("Record inserted")
#         conn.commit()
#     return True



def create_table():
    cur, _ = connection.connection('Plotly')
    cur.execute("CREATE TABLE GraphData (Id INT AUTO_INCREMENT PRIMARY KEY,\
         {} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25),{} varchar(25)\
        ,{} varchar(25)\
                                )".format('MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 
                                'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
                                'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',    
                                'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
                                'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',    
                                'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',       
                                'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
                                'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',    
                                'HeatingQC', 'CentralAir', 'Electrical', 'SalePrice')
                                )
    return True

def insertTable():
    cur, conn = connection.connection('Plotly')
    for i,row in df.iterrows():
        sql = "INSERT INTO Plotly.GraphData (MSSubClass, MSZoning, LotFrontage, LotArea, Street,\
            Alley, LotShape, LandContour, Utilities, LotConfig,LandSlope, Neighborhood, Condition1,\
            Condition2, BldgType,HouseStyle,OverallQual, OverallCond,YearBuilt,YearRemodAdd,\
            RoofStyle, RoofMatl, Exterior1st,Exterior2nd, MasVnrType,MasVnrArea, ExterQual, ExterCond,\
            Foundation, BsmtQual,BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinSF1,BsmtFinType2, BsmtFinSF2,BsmtUnfSF,\
            TotalBsmtSF, Heating,HeatingQC, CentralAir, Electrical,SalePrice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()
    return True


if __name__=="__main__":
    insertTable()