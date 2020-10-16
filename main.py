from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
# from src.model import spell_number
import uvicorn
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional
import pickle
from utilities.utility import *
from utilities.database import *



filename = 'model/house_price_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# cols_when_model_builds = loaded_model.get_booster().feature_names
# print("The need clolumns::::",cols_when_model_builds)

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


# @app.get('/')
# def read_form():
#     return 'hello world'


@app.get("/",response_class=HTMLResponse)
def read_form(request: Request):
	return templates.TemplateResponse('index.html', context={'request': request})


@app.post("/form")
def form_post(request: Request,region: str = Form(...),house_type: str = Form(...),square_feet: int = Form(...),
			  bed: int = Form(...),
			  bathroom: int = Form(...),cats: int = Form(...),dogs: int = Form(...),smoking: int = Form(...),
			  wheelchair: int = Form(...),electric: int = Form(...),furnished: int = Form(...),
			  laundry: str = Form(...),parking: str = Form(...),latitude: Optional[float] = Form(None),
			  longitude: Optional[float] = Form(None),state: str = Form(...)):
	
	region = str(region)
	if not latitude or longitude:
		latitude,longitude = region_lat_long(region)

	region = region_median_fun(region)
	state = state_median_fun(state)

	# for inserting in database
	insert_data([square_feet,bed,bathroom,cats,dogs,smoking,wheelchair,electric,furnished,latitude,longitude,region,state , house_type , laundry ,parking])


	house_type  = house(house_type)
	laundry = laundry_option(laundry)
	parking = parking_option(parking)


	input_data = [square_feet,bed,bathroom,cats,dogs,smoking,wheelchair,electric,furnished,latitude,longitude,region,state] + house_type + laundry + parking

	prediction = loaded_model.predict([input_data])
	# prediction = 'hello suraj'
	# print("length",len(input_data))
	
	# print("input data",input_data)
	return templates.TemplateResponse('output.html', context={'request': request, 'result': str(prediction[0])})


if __name__ == '__main__':
	uvicorn.run(app)




