from collections import defaultdict
import json

data = """Alabama
The State of Alabama comprises 67 counties.

Autauga County, Alabama
Baldwin County, Alabama
Barbour County, Alabama
Bibb County, Alabama
Blount County, Alabama
Bullock County, Alabama
Butler County, Alabama
Calhoun County, Alabama
Chambers County, Alabama
Cherokee County, Alabama
Chilton County, Alabama
Choctaw County, Alabama
Clarke County, Alabama
Clay County, Alabama
Cleburne County, Alabama
Coffee County, Alabama
Colbert County, Alabama
Conecuh County, Alabama
Coosa County, Alabama
Covington County, Alabama
Crenshaw County, Alabama
Cullman County, Alabama
Dale County, Alabama
Dallas County, Alabama
DeKalb County, Alabama
Elmore County, Alabama
Escambia County, Alabama
Etowah County, Alabama
Fayette County, Alabama
Franklin County, Alabama
Geneva County, Alabama
Greene County, Alabama
Hale County, Alabama
Henry County, Alabama
Houston County, Alabama
Jackson County, Alabama
Jefferson County, Alabama
Lamar County, Alabama
Lauderdale County, Alabama
Lawrence County, Alabama
Lee County, Alabama
Limestone County, Alabama
Lowndes County, Alabama
Macon County, Alabama
Madison County, Alabama
Marengo County, Alabama
Marion County, Alabama
Marshall County, Alabama
Mobile County, Alabama
Monroe County, Alabama
Montgomery County, Alabama
Morgan County, Alabama
Perry County, Alabama
Pickens County, Alabama
Pike County, Alabama
Randolph County, Alabama
Russell County, Alabama
Saint Clair County, Alabama
Shelby County, Alabama
Sumter County, Alabama
Talladega County, Alabama
Tallapoosa County, Alabama
Tuscaloosa County, Alabama
Walker County, Alabama
Washington County, Alabama
Wilcox County, Alabama
Winston County, Alabama
Alaska
The State of Alaska comprises 19 organized boroughs and 1 unorganized borough, the latter divided into 10 unorganized census areas.[3]

Aleutians East Borough, Alaska
Anchorage Borough, Alaska
Bristol Bay Borough, Alaska
Denali Borough, Alaska
Fairbanks North Star Borough, Alaska
Haines Borough, Alaska[4]
Juneau Borough, Alaska
Kenai Peninsula Borough, Alaska
Ketchikan Gateway Borough, Alaska
Kodiak Island Borough, Alaska
Lake and Peninsula Borough, Alaska
Matanuska-Susitna Borough, Alaska
North Slope Borough, Alaska
Northwest Arctic Borough, Alaska
Petersburg Borough, Alaska
Sitka Borough, Alaska
Skagway Borough, Alaska
Unorganized Borough, Alaska
Wrangell Borough, Alaska
Yakutat Borough, Alaska
Aleutians West Census Area, Alaska
Bethel Census Area, Alaska
Dillingham Census Area, Alaska
Hoonah-Angoon Census Area, Alaska
Kusilvak Census Area, Alaska
Nome Census Area, Alaska
Prince of Wales-Hyder Census Area, Alaska
Southeast Fairbanks Census Area, Alaska
Valdez-Cordova Census Area, Alaska
Yukon-Koyukuk Census Area, Alaska
American Samoa
The Territory of American Samoa has 14 counties; however, these counties are not counted by the U.S. Census Bureau (they are treated as minor civil divisions).[2] The U.S. Census Bureau counts the 3 districts and 2 atolls of American Samoa as county-equivalents.[1][2]

Eastern District, American Samoa
Manu'a District, American Samoa
Rose Atoll, American Samoa
Swains Island, American Samoa
Western District, American Samoa
Arizona
The State of Arizona comprises 15 counties.

Apache County, Arizona
Cochise County, Arizona
Coconino County, Arizona
Gila County, Arizona
Graham County, Arizona
Greenlee County, Arizona
La Paz County, Arizona
Maricopa County, Arizona
Mohave County, Arizona
Navajo County, Arizona
Pima County, Arizona
Pinal County, Arizona
Santa Cruz County, Arizona
Yavapai County, Arizona
Yuma County, Arizona
Arkansas
The State of Arkansas comprises 75 counties.

Arkansas County, Arkansas
Ashley County, Arkansas
Baxter County, Arkansas
Benton County, Arkansas
Boone County, Arkansas
Bradley County, Arkansas
Calhoun County, Arkansas
Carroll County, Arkansas
Chicot County, Arkansas
Clark County, Arkansas
Clay County, Arkansas
Cleburne County, Arkansas
Cleveland County, Arkansas
Columbia County, Arkansas
Conway County, Arkansas
Craighead County, Arkansas
Crawford County, Arkansas
Crittenden County, Arkansas
Cross County, Arkansas
Dallas County, Arkansas
Desha County, Arkansas
Drew County, Arkansas
Faulkner County, Arkansas
Franklin County, Arkansas
Fulton County, Arkansas
Garland County, Arkansas
Grant County, Arkansas
Greene County, Arkansas
Hempstead County, Arkansas
Hot Spring County, Arkansas
Howard County, Arkansas
Independence County, Arkansas
Izard County, Arkansas
Jackson County, Arkansas
Jefferson County, Arkansas
Johnson County, Arkansas
Lafayette County, Arkansas
Lawrence County, Arkansas
Lee County, Arkansas
Lincoln County, Arkansas
Little River County, Arkansas
Logan County, Arkansas
Lonoke County, Arkansas
Madison County, Arkansas
Marion County, Arkansas
Miller County, Arkansas
Mississippi County, Arkansas
Monroe County, Arkansas
Montgomery County, Arkansas
Nevada County, Arkansas
Newton County, Arkansas
Ouachita County, Arkansas
Perry County, Arkansas
Phillips County, Arkansas
Pike County, Arkansas
Poinsett County, Arkansas
Polk County, Arkansas
Pope County, Arkansas
Prairie County, Arkansas
Pulaski County, Arkansas
Randolph County, Arkansas
Saint Francis County, Arkansas
Saline County, Arkansas
Scott County, Arkansas
Searcy County, Arkansas
Sebastian County, Arkansas
Sevier County, Arkansas
Sharp County, Arkansas
Stone County, Arkansas
Union County, Arkansas
Van Buren County, Arkansas
Washington County, Arkansas
White County, Arkansas
Woodruff County, Arkansas
Yell County, Arkansas
California
The State of California comprises 58 counties, including one consolidated city-county government.

Alameda County, California
Alpine County, California
Amador County, California
Butte County, California
Calaveras County, California
Colusa County, California
Contra Costa County, California
Del Norte County, California
El Dorado County, California
Fresno County, California
Glenn County, California
Humboldt County, California
Imperial County, California
Inyo County, California
Kern County, California
Kings County, California
Lake County, California
Lassen County, California
Los Angeles County, California[5]
Madera County, California
Marin County, California
Mariposa County, California
Mendocino County, California
Merced County, California
Modoc County, California
Mono County, California
Monterey County, California
Napa County, California
Nevada County, California
Orange County, California
Placer County, California
Plumas County, California
Riverside County, California
Sacramento County, California
San Benito County, California
San Bernardino County, California
San Diego County, California
San Francisco County, California
San Joaquin County, California
San Luis Obispo County, California
San Mateo County, California
Santa Barbara County, California
Santa Clara County, California
Santa Cruz County, California
Shasta County, California
Sierra County, California
Siskiyou County, California
Solano County, California
Sonoma County, California
Stanislaus County, California
Sutter County, California
Tehama County, California
Trinity County, California
Tulare County, California
Tuolumne County, California
Ventura County, California
Yolo County, California
Yuba County, California
Colorado
The State of Colorado comprises 64 counties, including two consolidated city-county governments.

Adams County, Colorado
Alamosa County, Colorado
Arapahoe County, Colorado
Archuleta County, Colorado
Baca County, Colorado
Bent County, Colorado
Boulder County, Colorado
Broomfield County, Colorado
Chaffee County, Colorado
Cheyenne County, Colorado
Clear Creek County, Colorado
Conejos County, Colorado
Costilla County, Colorado
Crowley County, Colorado
Custer County, Colorado
Delta County, Colorado
Denver County, Colorado
Dolores County, Colorado
Douglas County, Colorado
Eagle County, Colorado
Elbert County, Colorado
El Paso County, Colorado
Fremont County, Colorado
Garfield County, Colorado
Gilpin County, Colorado
Grand County, Colorado
Gunnison County, Colorado
Hinsdale County, Colorado
Huerfano County, Colorado
Jackson County, Colorado
Jefferson County, Colorado
Kiowa County, Colorado
Kit Carson County, Colorado
Lake County, Colorado
La Plata County, Colorado
Larimer County, Colorado
Las Animas County, Colorado
Lincoln County, Colorado
Logan County, Colorado
Mesa County, Colorado
Mineral County, Colorado
Moffat County, Colorado
Montezuma County, Colorado
Montrose County, Colorado
Morgan County, Colorado
Otero County, Colorado
Ouray County, Colorado
Park County, Colorado
Phillips County, Colorado
Pitkin County, Colorado
Prowers County, Colorado
Pueblo County, Colorado
Rio Blanco County, Colorado
Rio Grande County, Colorado
Routt County, Colorado
Saguache County, Colorado
San Juan County, Colorado
San Miguel County, Colorado
Sedgwick County, Colorado
Summit County, Colorado
Teller County, Colorado
Washington County, Colorado
Weld County, Colorado
Yuma County, Colorado
Connecticut
The State of Connecticut comprises 8 counties.

Fairfield County, Connecticut
Hartford County, Connecticut
Litchfield County, Connecticut
Middlesex County, Connecticut
New Haven County, Connecticut
New London County, Connecticut
Tolland County, Connecticut
Windham County, Connecticut
Delaware
The State of Delaware comprises 3 counties.

Kent County, Delaware
New Castle County, Delaware
Sussex County, Delaware
District of Columbia
Main article: List of counties in the District of Columbia
See also: Wards of the District of Columbia
The United States Census Bureau and the Office of Management and Budget currently consider the District of Columbia to be a county-equivalent.

District of Columbia
Florida
The State of Florida comprises 67 counties.[6]

Alachua County, Florida
Baker County, Florida
Bay County, Florida
Bradford County, Florida
Brevard County, Florida
Broward County, Florida
Calhoun County, Florida
Charlotte County, Florida
Citrus County, Florida
Clay County, Florida
Collier County, Florida
Columbia County, Florida
DeSoto County, Florida
Dixie County, Florida
Duval County, Florida[7]
Escambia County, Florida
Flagler County, Florida
Franklin County, Florida
Gadsden County, Florida
Gilchrist County, Florida
Glades County, Florida
Gulf County, Florida
Hamilton County, Florida
Hardee County, Florida
Hendry County, Florida
Hernando County, Florida
Highlands County, Florida
Hillsborough County, Florida
Holmes County, Florida
Indian River County, Florida
Jackson County, Florida
Jefferson County, Florida
Lafayette County, Florida
Lake County, Florida
Lee County, Florida
Leon County, Florida
Levy County, Florida
Liberty County, Florida
Madison County, Florida
Manatee County, Florida
Marion County, Florida
Martin County, Florida
Miami-Dade County, Florida
Monroe County, Florida
Nassau County, Florida
Okaloosa County, Florida
Okeechobee County, Florida
Orange County, Florida
Osceola County, Florida
Palm Beach County, Florida
Pasco County, Florida
Pinellas County, Florida
Polk County, Florida
Putnam County, Florida
Saint Johns County, Florida
Saint Lucie County, Florida
Santa Rosa County, Florida
Sarasota County, Florida
Seminole County, Florida
Sumter County, Florida
Suwannee County, Florida
Taylor County, Florida
Union County, Florida
Volusia County, Florida
Wakulla County, Florida
Walton County, Florida
Washington County, Florida
Georgia
The State of Georgia comprises 159 counties.

Appling County, Georgia
Atkinson County, Georgia
Bacon County, Georgia
Baker County, Georgia
Baldwin County, Georgia
Banks County, Georgia
Barrow County, Georgia
Bartow County, Georgia
Ben Hill County, Georgia
Berrien County, Georgia
Bibb County, Georgia[8]
Bleckley County, Georgia
Brantley County, Georgia
Brooks County, Georgia
Bryan County, Georgia
Bulloch County, Georgia
Burke County, Georgia
Butts County, Georgia
Calhoun County, Georgia
Camden County, Georgia
Candler County, Georgia
Carroll County, Georgia
Catoosa County, Georgia
Charlton County, Georgia
Chatham County, Georgia
Chattahoochee County, Georgia[9]
Chattooga County, Georgia
Cherokee County, Georgia
Clarke County, Georgia[10]
Clay County, Georgia
Clayton County, Georgia
Clinch County, Georgia
Cobb County, Georgia
Coffee County, Georgia
Colquitt County, Georgia
Columbia County, Georgia
Cook County, Georgia
Coweta County, Georgia
Crawford County, Georgia
Crisp County, Georgia
Dade County, Georgia
Dawson County, Georgia
Decatur County, Georgia
DeKalb County, Georgia
Dodge County, Georgia
Dooly County, Georgia
Dougherty County, Georgia
Douglas County, Georgia
Early County, Georgia
Echols County, Georgia[11]
Effingham County, Georgia
Elbert County, Georgia
Emanuel County, Georgia
Evans County, Georgia
Fannin County, Georgia
Fayette County, Georgia
Floyd County, Georgia
Forsyth County, Georgia
Franklin County, Georgia
Fulton County, Georgia
Gilmer County, Georgia
Glascock County, Georgia
Glynn County, Georgia
Gordon County, Georgia
Grady County, Georgia
Greene County, Georgia
Gwinnett County, Georgia
Habersham County, Georgia
Hall County, Georgia
Hancock County, Georgia
Haralson County, Georgia
Harris County, Georgia
Hart County, Georgia
Heard County, Georgia
Henry County, Georgia
Houston County, Georgia
Irwin County, Georgia
Jackson County, Georgia
Jasper County, Georgia
Jeff Davis County, Georgia
Jefferson County, Georgia
Jenkins County, Georgia
Johnson County, Georgia
Jones County, Georgia
Lamar County, Georgia
Lanier County, Georgia
Laurens County, Georgia
Lee County, Georgia
Liberty County, Georgia
Lincoln County, Georgia
Long County, Georgia
Lowndes County, Georgia
Lumpkin County, Georgia
McDuffie County, Georgia
McIntosh County, Georgia
Macon County, Georgia
Madison County, Georgia
Marion County, Georgia
Meriwether County, Georgia
Miller County, Georgia
Mitchell County, Georgia
Monroe County, Georgia
Montgomery County, Georgia
Morgan County, Georgia
Murray County, Georgia
Muscogee County, Georgia[12]
Newton County, Georgia
Oconee County, Georgia
Oglethorpe County, Georgia
Paulding County, Georgia
Peach County, Georgia
Pickens County, Georgia
Pierce County, Georgia
Pike County, Georgia
Polk County, Georgia
Pulaski County, Georgia
Putnam County, Georgia
Quitman County, Georgia[13]
Rabun County, Georgia
Randolph County, Georgia
Richmond County, Georgia[14]
Rockdale County, Georgia
Schley County, Georgia
Screven County, Georgia
Seminole County, Georgia
Spalding County, Georgia
Stephens County, Georgia
Stewart County, Georgia
Sumter County, Georgia
Talbot County, Georgia
Taliaferro County, Georgia
Tattnall County, Georgia
Taylor County, Georgia
Telfair County, Georgia
Terrell County, Georgia
Thomas County, Georgia
Tift County, Georgia
Toombs County, Georgia
Towns County, Georgia
Treutlen County, Georgia
Troup County, Georgia
Turner County, Georgia
Twiggs County, Georgia
Union County, Georgia
Upson County, Georgia
Walker County, Georgia
Walton County, Georgia
Ware County, Georgia
Warren County, Georgia
Washington County, Georgia
Wayne County, Georgia
Webster County, Georgia[15]
Wheeler County, Georgia
White County, Georgia
Whitfield County, Georgia
Wilcox County, Georgia
Wilkes County, Georgia
Wilkinson County, Georgia
Worth County, Georgia
Guam
The Territory of Guam has no counties. The U.S. Census Bureau counts all of Guam as one county-equivalent.[1][2]

Guam
Hawaii
The State of Hawaii comprises 5 counties.

Hawaii County, Hawaii
Honolulu County, Hawaii
Kalawao County, Hawaii[16]
Kauai County, Hawaii
Maui County, Hawaii
Idaho
The State of Idaho comprises 44 counties.

Ada County, Idaho
Adams County, Idaho
Bannock County, Idaho
Bear Lake County, Idaho
Benewah County, Idaho
Bingham County, Idaho
Blaine County, Idaho
Boise County, Idaho
Bonner County, Idaho
Bonneville County, Idaho
Boundary County, Idaho
Butte County, Idaho
Camas County, Idaho
Canyon County, Idaho
Caribou County, Idaho
Cassia County, Idaho
Clark County, Idaho
Clearwater County, Idaho
Custer County, Idaho
Elmore County, Idaho
Franklin County, Idaho
Fremont County, Idaho
Gem County, Idaho
Gooding County, Idaho
Idaho County, Idaho
Jefferson County, Idaho
Jerome County, Idaho
Kootenai County, Idaho
Latah County, Idaho
Lemhi County, Idaho
Lewis County, Idaho
Lincoln County, Idaho
Madison County, Idaho
Minidoka County, Idaho
Nez Perce County, Idaho
Oneida County, Idaho
Owyhee County, Idaho
Payette County, Idaho
Power County, Idaho
Shoshone County, Idaho
Teton County, Idaho
Twin Falls County, Idaho
Valley County, Idaho
Washington County, Idaho
Illinois
The State of Illinois comprises 102 counties.

Adams County, Illinois
Alexander County, Illinois
Bond County, Illinois
Boone County, Illinois
Brown County, Illinois
Bureau County, Illinois
Calhoun County, Illinois
Carroll County, Illinois
Cass County, Illinois
Champaign County, Illinois
Christian County, Illinois
Clark County, Illinois
Clay County, Illinois
Clinton County, Illinois
Coles County, Illinois
Cook County, Illinois
Crawford County, Illinois
Cumberland County, Illinois
DeKalb County, Illinois
DeWitt County, Illinois
Douglas County, Illinois
DuPage County, Illinois
Edgar County, Illinois
Edwards County, Illinois
Effingham County, Illinois
Fayette County, Illinois
Ford County, Illinois
Franklin County, Illinois
Fulton County, Illinois
Gallatin County, Illinois
Greene County, Illinois
Grundy County, Illinois
Hamilton County, Illinois
Hancock County, Illinois
Hardin County, Illinois
Henderson County, Illinois
Henry County, Illinois
Iroquois County, Illinois
Jackson County, Illinois
Jasper County, Illinois
Jefferson County, Illinois
Jersey County, Illinois
Jo Daviess County, Illinois
Johnson County, Illinois
Kane County, Illinois
Kankakee County, Illinois
Kendall County, Illinois
Knox County, Illinois
Lake County, Illinois
LaSalle County, Illinois
Lawrence County, Illinois
Lee County, Illinois
Livingston County, Illinois
Logan County, Illinois
McDonough County, Illinois
McHenry County, Illinois
McLean County, Illinois
Macon County, Illinois
Macoupin County, Illinois
Madison County, Illinois
Marion County, Illinois
Marshall County, Illinois
Mason County, Illinois
Massac County, Illinois
Menard County, Illinois
Mercer County, Illinois
Monroe County, Illinois
Montgomery County, Illinois
Morgan County, Illinois
Moultrie County, Illinois
Ogle County, Illinois
Peoria County, Illinois
Perry County, Illinois
Piatt County, Illinois
Pike County, Illinois
Pope County, Illinois
Pulaski County, Illinois
Putnam County, Illinois
Randolph County, Illinois
Richland County, Illinois
Rock Island County, Illinois
Saint Clair County, Illinois
Saline County, Illinois
Sangamon County, Illinois
Schuyler County, Illinois
Scott County, Illinois
Shelby County, Illinois
Stark County, Illinois
Stephenson County, Illinois
Tazewell County, Illinois
Union County, Illinois
Vermilion County, Illinois
Wabash County, Illinois
Warren County, Illinois
Washington County, Illinois
Wayne County, Illinois
White County, Illinois
Whiteside County, Illinois
Will County, Illinois
Williamson County, Illinois
Winnebago County, Illinois
Woodford County, Illinois
Indiana
The State of Indiana comprises 92 counties.

Adams County, Indiana
Allen County, Indiana
Bartholomew County, Indiana
Benton County, Indiana
Blackford County, Indiana
Boone County, Indiana
Brown County, Indiana
Carroll County, Indiana
Cass County, Indiana
Clark County, Indiana
Clay County, Indiana
Clinton County, Indiana
Crawford County, Indiana
Daviess County, Indiana
Dearborn County, Indiana
Decatur County, Indiana
DeKalb County, Indiana
Delaware County, Indiana
Dubois County, Indiana
Elkhart County, Indiana
Fayette County, Indiana
Floyd County, Indiana
Fountain County, Indiana
Franklin County, Indiana
Fulton County, Indiana
Gibson County, Indiana
Grant County, Indiana
Greene County, Indiana
Hamilton County, Indiana
Hancock County, Indiana
Harrison County, Indiana
Hendricks County, Indiana
Henry County, Indiana
Howard County, Indiana
Huntington County, Indiana
Jackson County, Indiana
Jasper County, Indiana
Jay County, Indiana
Jefferson County, Indiana
Jennings County, Indiana
Johnson County, Indiana
Knox County, Indiana
Kosciusko County, Indiana
LaGrange County, Indiana
Lake County, Indiana
LaPorte County, Indiana
Lawrence County, Indiana
Madison County, Indiana
Marion County, Indiana[17]
Marshall County, Indiana
Martin County, Indiana
Miami County, Indiana
Monroe County, Indiana
Montgomery County, Indiana
Morgan County, Indiana
Newton County, Indiana
Noble County, Indiana
Ohio County, Indiana
Orange County, Indiana
Owen County, Indiana
Parke County, Indiana
Perry County, Indiana
Pike County, Indiana
Porter County, Indiana
Posey County, Indiana
Pulaski County, Indiana
Putnam County, Indiana
Randolph County, Indiana
Ripley County, Indiana
Rush County, Indiana
Saint Joseph County, Indiana
Scott County, Indiana
Shelby County, Indiana
Spencer County, Indiana
Starke County, Indiana
Steuben County, Indiana
Sullivan County, Indiana
Switzerland County, Indiana
Tippecanoe County, Indiana
Tipton County, Indiana
Union County, Indiana
Vanderburgh County, Indiana
Vermillion County, Indiana
Vigo County, Indiana
Wabash County, Indiana
Warren County, Indiana
Warrick County, Indiana
Washington County, Indiana
Wayne County, Indiana
Wells County, Indiana
White County, Indiana
Whitley County, Indiana
Iowa
The State of Iowa comprises 99 counties.

Adair County, Iowa
Adams County, Iowa
Allamakee County, Iowa
Appanoose County, Iowa
Audubon County, Iowa
Benton County, Iowa
Black Hawk County, Iowa
Boone County, Iowa
Bremer County, Iowa
Buchanan County, Iowa
Buena Vista County, Iowa
Butler County, Iowa
Calhoun County, Iowa
Carroll County, Iowa
Cass County, Iowa
Cedar County, Iowa
Cerro Gordo County, Iowa
Cherokee County, Iowa
Chickasaw County, Iowa
Clarke County, Iowa
Clay County, Iowa
Clayton County, Iowa
Clinton County, Iowa
Crawford County, Iowa
Dallas County, Iowa
Davis County, Iowa
Decatur County, Iowa
Delaware County, Iowa
Des Moines County, Iowa
Dickinson County, Iowa
Dubuque County, Iowa
Emmet County, Iowa
Fayette County, Iowa
Floyd County, Iowa
Franklin County, Iowa
Fremont County, Iowa
Greene County, Iowa
Grundy County, Iowa
Guthrie County, Iowa
Hamilton County, Iowa
Hancock County, Iowa
Hardin County, Iowa
Harrison County, Iowa
Henry County, Iowa
Howard County, Iowa
Humboldt County, Iowa
Ida County, Iowa
Iowa County, Iowa
Jackson County, Iowa
Jasper County, Iowa
Jefferson County, Iowa
Johnson County, Iowa
Jones County, Iowa
Keokuk County, Iowa
Kossuth County, Iowa
Lee County, Iowa
Linn County, Iowa
Louisa County, Iowa
Lucas County, Iowa
Lyon County, Iowa
Madison County, Iowa
Mahaska County, Iowa
Marion County, Iowa
Marshall County, Iowa
Mills County, Iowa
Mitchell County, Iowa
Monona County, Iowa
Monroe County, Iowa
Montgomery County, Iowa
Muscatine County, Iowa
O'Brien County, Iowa
Osceola County, Iowa
Page County, Iowa
Palo Alto County, Iowa
Plymouth County, Iowa
Pocahontas County, Iowa
Polk County, Iowa
Pottawattamie County, Iowa
Poweshiek County, Iowa
Ringgold County, Iowa
Sac County, Iowa
Scott County, Iowa
Shelby County, Iowa
Sioux County, Iowa
Story County, Iowa
Tama County, Iowa
Taylor County, Iowa
Union County, Iowa
Van Buren County, Iowa
Wapello County, Iowa
Warren County, Iowa
Washington County, Iowa
Wayne County, Iowa
Webster County, Iowa
Winnebago County, Iowa
Winneshiek County, Iowa
Woodbury County, Iowa
Worth County, Iowa
Wright County, Iowa
Kansas
The State of Kansas comprises 105 counties.

Allen County, Kansas
Anderson County, Kansas
Atchison County, Kansas
Barber County, Kansas
Barton County, Kansas
Bourbon County, Kansas
Brown County, Kansas
Butler County, Kansas
Chase County, Kansas
Chautauqua County, Kansas
Cherokee County, Kansas
Cheyenne County, Kansas
Clark County, Kansas
Clay County, Kansas
Cloud County, Kansas
Coffey County, Kansas
Comanche County, Kansas
Cowley County, Kansas
Crawford County, Kansas
Decatur County, Kansas
Dickinson County, Kansas
Doniphan County, Kansas
Douglas County, Kansas
Edwards County, Kansas
Elk County, Kansas
Ellis County, Kansas
Ellsworth County, Kansas
Finney County, Kansas
Ford County, Kansas
Franklin County, Kansas
Geary County, Kansas
Gove County, Kansas
Graham County, Kansas
Grant County, Kansas
Gray County, Kansas
Greeley County, Kansas
Greenwood County, Kansas
Hamilton County, Kansas
Harper County, Kansas
Harvey County, Kansas
Haskell County, Kansas
Hodgeman County, Kansas
Jackson County, Kansas
Jefferson County, Kansas
Jewell County, Kansas
Johnson County, Kansas
Kearny County, Kansas
Kingman County, Kansas
Kiowa County, Kansas
Labette County, Kansas
Lane County, Kansas
Leavenworth County, Kansas
Lincoln County, Kansas
Linn County, Kansas
Logan County, Kansas
Lyon County, Kansas
McPherson County, Kansas
Marion County, Kansas
Marshall County, Kansas
Meade County, Kansas
Miami County, Kansas
Mitchell County, Kansas
Montgomery County, Kansas
Morris County, Kansas
Morton County, Kansas
Nemaha County, Kansas
Neosho County, Kansas
Ness County, Kansas
Norton County, Kansas
Osage County, Kansas
Osborne County, Kansas
Ottawa County, Kansas
Pawnee County, Kansas
Phillips County, Kansas
Pottawatomie County, Kansas
Pratt County, Kansas
Rawlins County, Kansas
Reno County, Kansas
Republic County, Kansas
Rice County, Kansas
Riley County, Kansas
Rooks County, Kansas
Rush County, Kansas
Russell County, Kansas
Saline County, Kansas
Scott County, Kansas
Sedgwick County, Kansas
Seward County, Kansas
Shawnee County, Kansas
Sheridan County, Kansas
Sherman County, Kansas
Smith County, Kansas
Stafford County, Kansas
Stanton County, Kansas
Stevens County, Kansas
Sumner County, Kansas
Thomas County, Kansas
Trego County, Kansas
Wabaunsee County, Kansas
Wallace County, Kansas
Washington County, Kansas
Wichita County, Kansas
Wilson County, Kansas
Woodson County, Kansas
Wyandotte County, Kansas
Kentucky
The Commonwealth of Kentucky comprises 120 counties.

Adair County, Kentucky
Allen County, Kentucky
Anderson County, Kentucky
Ballard County, Kentucky
Barren County, Kentucky
Bath County, Kentucky
Bell County, Kentucky
Boone County, Kentucky
Bourbon County, Kentucky
Boyd County, Kentucky
Boyle County, Kentucky
Bracken County, Kentucky
Breathitt County, Kentucky
Breckinridge County, Kentucky
Bullitt County, Kentucky
Butler County, Kentucky
Caldwell County, Kentucky
Calloway County, Kentucky
Campbell County, Kentucky
Carlisle County, Kentucky
Carroll County, Kentucky
Carter County, Kentucky
Casey County, Kentucky
Christian County, Kentucky
Clark County, Kentucky
Clay County, Kentucky
Clinton County, Kentucky
Crittenden County, Kentucky
Cumberland County, Kentucky
Daviess County, Kentucky
Edmonson County, Kentucky
Elliott County, Kentucky
Estill County, Kentucky
Fayette County, Kentucky[18]
Fleming County, Kentucky
Floyd County, Kentucky
Franklin County, Kentucky
Fulton County, Kentucky
Gallatin County, Kentucky
Garrard County, Kentucky
Grant County, Kentucky
Graves County, Kentucky
Grayson County, Kentucky
Green County, Kentucky
Greenup County, Kentucky
Hancock County, Kentucky
Hardin County, Kentucky
Harlan County, Kentucky
Harrison County, Kentucky
Hart County, Kentucky
Henderson County, Kentucky
Henry County, Kentucky
Hickman County, Kentucky
Hopkins County, Kentucky
Jackson County, Kentucky
Jefferson County, Kentucky[19]
Jessamine County, Kentucky
Johnson County, Kentucky
Kenton County, Kentucky
Knott County, Kentucky
Knox County, Kentucky
LaRue County, Kentucky
Laurel County, Kentucky
Lawrence County, Kentucky
Lee County, Kentucky
Leslie County, Kentucky
Letcher County, Kentucky
Lewis County, Kentucky
Lincoln County, Kentucky
Livingston County, Kentucky
Logan County, Kentucky
Lyon County, Kentucky
McCracken County, Kentucky
McCreary County, Kentucky
McLean County, Kentucky
Madison County, Kentucky
Magoffin County, Kentucky
Marion County, Kentucky
Marshall County, Kentucky
Martin County, Kentucky
Mason County, Kentucky
Meade County, Kentucky
Menifee County, Kentucky
Mercer County, Kentucky
Metcalfe County, Kentucky
Monroe County, Kentucky
Montgomery County, Kentucky
Morgan County, Kentucky
Muhlenberg County, Kentucky
Nelson County, Kentucky
Nicholas County, Kentucky
Ohio County, Kentucky
Oldham County, Kentucky
Owen County, Kentucky
Owsley County, Kentucky
Pendleton County, Kentucky
Perry County, Kentucky
Pike County, Kentucky
Powell County, Kentucky
Pulaski County, Kentucky
Robertson County, Kentucky
Rockcastle County, Kentucky
Rowan County, Kentucky
Russell County, Kentucky
Scott County, Kentucky
Shelby County, Kentucky
Simpson County, Kentucky
Spencer County, Kentucky
Taylor County, Kentucky
Todd County, Kentucky
Trigg County, Kentucky
Trimble County, Kentucky
Union County, Kentucky
Warren County, Kentucky
Washington County, Kentucky
Wayne County, Kentucky
Webster County, Kentucky
Whitley County, Kentucky
Wolfe County, Kentucky
Woodford County, Kentucky
Louisiana
The State of Louisiana comprises 64 parishes.[20]

Acadia Parish, Louisiana
Allen Parish, Louisiana
Ascension Parish, Louisiana
Assumption Parish, Louisiana
Avoyelles Parish, Louisiana
Beauregard Parish, Louisiana
Bienville Parish, Louisiana
Bossier Parish, Louisiana
Caddo Parish, Louisiana
Calcasieu Parish, Louisiana
Caldwell Parish, Louisiana
Cameron Parish, Louisiana
Catahoula Parish, Louisiana
Claiborne Parish, Louisiana
Concordia Parish, Louisiana
DeSoto Parish, Louisiana
East Baton Rouge Parish, Louisiana
East Carroll Parish, Louisiana
East Feliciana Parish, Louisiana
Evangeline Parish, Louisiana
Franklin Parish, Louisiana
Grant Parish, Louisiana
Iberia Parish, Louisiana
Iberville Parish, Louisiana
Jackson Parish, Louisiana
Jefferson Parish, Louisiana
Jefferson Davis Parish, Louisiana
Lafayette Parish, Louisiana
Lafourche Parish, Louisiana
LaSalle Parish, Louisiana
Lincoln Parish, Louisiana
Livingston Parish, Louisiana
Madison Parish, Louisiana
Morehouse Parish, Louisiana
Natchitoches Parish, Louisiana
Orleans Parish, Louisiana
Ouachita Parish, Louisiana
Plaquemines Parish, Louisiana
Pointe Coupee Parish, Louisiana
Rapides Parish, Louisiana
Red River Parish, Louisiana
Richland Parish, Louisiana
Sabine Parish, Louisiana
Saint Bernard Parish, Louisiana
Saint Charles Parish, Louisiana
Saint Helena Parish, Louisiana
Saint James Parish, Louisiana
Saint John the Baptist Parish, Louisiana
Saint Landry Parish, Louisiana
Saint Martin Parish, Louisiana
Saint Mary Parish, Louisiana
Saint Tammany Parish, Louisiana
Tangipahoa Parish, Louisiana
Tensas Parish, Louisiana
Terrebonne Parish, Louisiana[21]
Union Parish, Louisiana
Vermilion Parish, Louisiana
Vernon Parish, Louisiana
Washington Parish, Louisiana
Webster Parish, Louisiana
West Baton Rouge Parish, Louisiana
West Carroll Parish, Louisiana
West Feliciana Parish, Louisiana
Winn Parish, Louisiana
Maine
The State of Maine comprises 16 counties.

Androscoggin County, Maine
Aroostook County, Maine
Cumberland County, Maine
Franklin County, Maine
Hancock County, Maine
Kennebec County, Maine
Knox County, Maine
Lincoln County, Maine
Oxford County, Maine
Penobscot County, Maine
Piscataquis County, Maine
Sagadahoc County, Maine
Somerset County, Maine
Waldo County, Maine
Washington County, Maine
York County, Maine
Maryland
The State of Maryland comprises 23 counties and 1 independent city.

Allegany County, Maryland
Anne Arundel County, Maryland
Baltimore County, Maryland
Baltimore City, Maryland
Calvert County, Maryland
Caroline County, Maryland
Carroll County, Maryland
Cecil County, Maryland
Charles County, Maryland
Dorchester County, Maryland
Frederick County, Maryland
Garrett County, Maryland
Harford County, Maryland
Howard County, Maryland
Kent County, Maryland
Montgomery County, Maryland
Prince George's County, Maryland
Queen Anne's County, Maryland
Saint Mary's County, Maryland
Somerset County, Maryland
Talbot County, Maryland
Washington County, Maryland
Wicomico County, Maryland
Worcester County, Maryland
Massachusetts
The Commonwealth of Massachusetts comprises 14 counties, including one consolidated city-county government.

Barnstable County, Massachusetts
Berkshire County, Massachusetts[22]
Bristol County, Massachusetts
Dukes County, Massachusetts
Essex County, Massachusetts[23]
Franklin County, Massachusetts[24]
Hampden County, Massachusetts[25]
Hampshire County, Massachusetts[26]
Middlesex County, Massachusetts[27]
Nantucket County, Massachusetts
Norfolk County, Massachusetts
Plymouth County, Massachusetts
Suffolk County, Massachusetts[28]
Worcester County, Massachusetts[29]
Michigan
The State of Michigan comprises 83 counties.

Alcona County, Michigan
Alger County, Michigan
Allegan County, Michigan
Alpena County, Michigan
Antrim County, Michigan
Arenac County, Michigan
Baraga County, Michigan
Barry County, Michigan
Bay County, Michigan
Benzie County, Michigan
Berrien County, Michigan
Branch County, Michigan
Calhoun County, Michigan
Cass County, Michigan
Charlevoix County, Michigan
Cheboygan County, Michigan
Chippewa County, Michigan
Clare County, Michigan
Clinton County, Michigan
Crawford County, Michigan
Delta County, Michigan
Dickinson County, Michigan
Eaton County, Michigan
Emmet County, Michigan
Genesee County, Michigan
Gladwin County, Michigan
Gogebic County, Michigan
Grand Traverse County, Michigan
Gratiot County, Michigan
Hillsdale County, Michigan
Houghton County, Michigan
Huron County, Michigan
Ingham County, Michigan
Ionia County, Michigan
Iosco County, Michigan
Iron County, Michigan
Isabella County, Michigan
Jackson County, Michigan
Kalamazoo County, Michigan
Kalkaska County, Michigan
Kent County, Michigan
Keweenaw County, Michigan
Lake County, Michigan
Lapeer County, Michigan
Leelanau County, Michigan
Lenawee County, Michigan
Livingston County, Michigan
Luce County, Michigan
Mackinac County, Michigan
Macomb County, Michigan
Manistee County, Michigan
Marquette County, Michigan
Mason County, Michigan
Mecosta County, Michigan
Menominee County, Michigan
Midland County, Michigan
Missaukee County, Michigan
Monroe County, Michigan
Montcalm County, Michigan
Montmorency County, Michigan
Muskegon County, Michigan
Newaygo County, Michigan
Oakland County, Michigan
Oceana County, Michigan
Ogemaw County, Michigan
Ontonagon County, Michigan
Osceola County, Michigan
Oscoda County, Michigan
Otsego County, Michigan
Ottawa County, Michigan
Presque Isle County, Michigan
Roscommon County, Michigan
Saginaw County, Michigan
Saint Clair County, Michigan
Saint Joseph County, Michigan
Sanilac County, Michigan
Schoolcraft County, Michigan
Shiawassee County, Michigan
Tuscola County, Michigan
Van Buren County, Michigan
Washtenaw County, Michigan
Wayne County, Michigan
Wexford County, Michigan
Minnesota
The State of Minnesota comprises 87 counties.

Aitkin County, Minnesota
Anoka County, Minnesota
Becker County, Minnesota
Beltrami County, Minnesota
Benton County, Minnesota
Big Stone County, Minnesota
Blue Earth County, Minnesota
Brown County, Minnesota
Carlton County, Minnesota
Carver County, Minnesota
Cass County, Minnesota
Chippewa County, Minnesota
Chisago County, Minnesota
Clay County, Minnesota
Clearwater County, Minnesota
Cook County, Minnesota
Cottonwood County, Minnesota
Crow Wing County, Minnesota
Dakota County, Minnesota
Dodge County, Minnesota
Douglas County, Minnesota
Faribault County, Minnesota
Fillmore County, Minnesota
Freeborn County, Minnesota
Goodhue County, Minnesota
Grant County, Minnesota
Hennepin County, Minnesota
Houston County, Minnesota
Hubbard County, Minnesota
Isanti County, Minnesota
Itasca County, Minnesota
Jackson County, Minnesota
Kanabec County, Minnesota
Kandiyohi County, Minnesota
Kittson County, Minnesota
Koochiching County, Minnesota
Lac qui Parle County, Minnesota
Lake County, Minnesota
Lake of the Woods County, Minnesota
LeSueur County, Minnesota
Lincoln County, Minnesota
Lyon County, Minnesota
McLeod County, Minnesota
Mahnomen County, Minnesota
Marshall County, Minnesota
Martin County, Minnesota
Meeker County, Minnesota
Mille Lacs County, Minnesota
Morrison County, Minnesota
Mower County, Minnesota
Murray County, Minnesota
Nicollet County, Minnesota
Nobles County, Minnesota
Norman County, Minnesota
Olmsted County, Minnesota
Otter Tail County, Minnesota
Pennington County, Minnesota
Pine County, Minnesota
Pipestone County, Minnesota
Polk County, Minnesota
Pope County, Minnesota
Ramsey County, Minnesota
Red Lake County, Minnesota
Redwood County, Minnesota
Renville County, Minnesota
Rice County, Minnesota
Rock County, Minnesota
Roseau County, Minnesota
Saint Louis County, Minnesota
Scott County, Minnesota
Sherburne County, Minnesota
Sibley County, Minnesota
Stearns County, Minnesota
Steele County, Minnesota
Stevens County, Minnesota
Swift County, Minnesota
Todd County, Minnesota
Traverse County, Minnesota
Wabasha County, Minnesota
Wadena County, Minnesota
Waseca County, Minnesota
Washington County, Minnesota
Watonwan County, Minnesota
Wilkin County, Minnesota
Winona County, Minnesota
Wright County, Minnesota
Yellow Medicine County, Minnesota
Mississippi
The State of Mississippi comprises 82 counties.

Adams County, Mississippi
Alcorn County, Mississippi
Amite County, Mississippi
Attala County, Mississippi
Benton County, Mississippi
Bolivar County, Mississippi
Calhoun County, Mississippi
Carroll County, Mississippi
Chickasaw County, Mississippi
Choctaw County, Mississippi
Claiborne County, Mississippi
Clarke County, Mississippi
Clay County, Mississippi
Coahoma County, Mississippi
Copiah County, Mississippi
Covington County, Mississippi
DeSoto County, Mississippi
Forrest County, Mississippi
Franklin County, Mississippi
George County, Mississippi
Greene County, Mississippi
Grenada County, Mississippi
Hancock County, Mississippi
Harrison County, Mississippi
Hinds County, Mississippi
Holmes County, Mississippi
Humphreys County, Mississippi
Issaquena County, Mississippi
Itawamba County, Mississippi
Jackson County, Mississippi
Jasper County, Mississippi
Jefferson County, Mississippi
Jefferson Davis County, Mississippi
Jones County, Mississippi
Kemper County, Mississippi
Lafayette County, Mississippi
Lamar County, Mississippi
Lauderdale County, Mississippi
Lawrence County, Mississippi
Leake County, Mississippi
Lee County, Mississippi
Leflore County, Mississippi
Lincoln County, Mississippi
Lowndes County, Mississippi
Madison County, Mississippi
Marion County, Mississippi
Marshall County, Mississippi
Monroe County, Mississippi
Montgomery County, Mississippi
Neshoba County, Mississippi
Newton County, Mississippi
Noxubee County, Mississippi
Oktibbeha County, Mississippi
Panola County, Mississippi
Pearl River County, Mississippi
Perry County, Mississippi
Pike County, Mississippi
Pontotoc County, Mississippi
Prentiss County, Mississippi
Quitman County, Mississippi
Rankin County, Mississippi
Scott County, Mississippi
Sharkey County, Mississippi
Simpson County, Mississippi
Smith County, Mississippi
Stone County, Mississippi
Sunflower County, Mississippi
Tallahatchie County, Mississippi
Tate County, Mississippi
Tippah County, Mississippi
Tishomingo County, Mississippi
Tunica County, Mississippi
Union County, Mississippi
Walthall County, Mississippi
Warren County, Mississippi
Washington County, Mississippi
Wayne County, Mississippi
Webster County, Mississippi
Wilkinson County, Mississippi
Winston County, Mississippi
Yalobusha County, Mississippi
Yazoo County, Mississippi
Missouri
The State of Missouri comprises 114 counties and one independent city.

Adair County, Missouri
Andrew County, Missouri
Atchison County, Missouri
Audrain County, Missouri
Barry County, Missouri
Barton County, Missouri
Bates County, Missouri
Benton County, Missouri
Bollinger County, Missouri
Boone County, Missouri
Buchanan County, Missouri
Butler County, Missouri
Caldwell County, Missouri
Callaway County, Missouri
Camden County, Missouri
Cape Girardeau County, Missouri
Carroll County, Missouri
Carter County, Missouri
Cass County, Missouri
Cedar County, Missouri
Chariton County, Missouri
Christian County, Missouri
Clark County, Missouri
Clay County, Missouri
Clinton County, Missouri
Cole County, Missouri
Cooper County, Missouri
Crawford County, Missouri
Dade County, Missouri
Dallas County, Missouri
Daviess County, Missouri
DeKalb County, Missouri
Dent County, Missouri
Douglas County, Missouri
Dunklin County, Missouri
Franklin County, Missouri
Gasconade County, Missouri
Gentry County, Missouri
Greene County, Missouri
Grundy County, Missouri
Harrison County, Missouri
Henry County, Missouri
Hickory County, Missouri
Holt County, Missouri
Howard County, Missouri
Howell County, Missouri
Iron County, Missouri
Jackson County, Missouri
Jasper County, Missouri
Jefferson County, Missouri
Johnson County, Missouri
Knox County, Missouri
Laclede County, Missouri
Lafayette County, Missouri
Lawrence County, Missouri
Lewis County, Missouri
Lincoln County, Missouri
Linn County, Missouri
Livingston County, Missouri
McDonald County, Missouri
Macon County, Missouri
Madison County, Missouri
Maries County, Missouri
Marion County, Missouri
Mercer County, Missouri
Miller County, Missouri
Mississippi County, Missouri
Moniteau County, Missouri
Monroe County, Missouri
Montgomery County, Missouri
Morgan County, Missouri
New Madrid County, Missouri
Newton County, Missouri
Nodaway County, Missouri
Oregon County, Missouri
Osage County, Missouri
Ozark County, Missouri
Pemiscot County, Missouri
Perry County, Missouri
Pettis County, Missouri
Phelps County, Missouri
Pike County, Missouri
Platte County, Missouri
Polk County, Missouri
Pulaski County, Missouri
Putnam County, Missouri
Ralls County, Missouri
Randolph County, Missouri
Ray County, Missouri
Reynolds County, Missouri
Ripley County, Missouri
Saint Charles County, Missouri
Saint Clair County, Missouri
Saint Francois County, Missouri
Saint Louis County, Missouri
Saint Louis City, Missouri
Sainte Genevieve County, Missouri
Saline County, Missouri
Schuyler County, Missouri
Scotland County, Missouri
Scott County, Missouri
Shannon County, Missouri
Shelby County, Missouri
Stoddard County, Missouri
Stone County, Missouri
Sullivan County, Missouri
Taney County, Missouri
Texas County, Missouri
Vernon County, Missouri
Warren County, Missouri
Washington County, Missouri
Wayne County, Missouri
Webster County, Missouri
Worth County, Missouri
Wright County, Missouri
Montana
The State of Montana comprises 56 counties.

Beaverhead County, Montana
Big Horn County, Montana
Blaine County, Montana
Broadwater County, Montana
Carbon County, Montana
Carter County, Montana
Cascade County, Montana
Chouteau County, Montana
Custer County, Montana
Daniels County, Montana
Dawson County, Montana
Deer Lodge County, Montana[30]
Fallon County, Montana
Fergus County, Montana
Flathead County, Montana
Gallatin County, Montana
Garfield County, Montana
Glacier County, Montana
Golden Valley County, Montana
Granite County, Montana
Hill County, Montana
Jefferson County, Montana
Judith Basin County, Montana
Lake County, Montana
Lewis and Clark County, Montana
Liberty County, Montana
Lincoln County, Montana
McCone County, Montana
Madison County, Montana
Meagher County, Montana
Mineral County, Montana
Missoula County, Montana
Musselshell County, Montana
Park County, Montana
Petroleum County, Montana
Phillips County, Montana
Pondera County, Montana
Powder River County, Montana
Powell County, Montana
Prairie County, Montana
Ravalli County, Montana
Richland County, Montana
Roosevelt County, Montana
Rosebud County, Montana
Sanders County, Montana
Sheridan County, Montana
Silver Bow County, Montana[31]
Stillwater County, Montana
Sweet Grass County, Montana
Teton County, Montana
Toole County, Montana
Treasure County, Montana
Valley County, Montana
Wheatland County, Montana
Wibaux County, Montana
Yellowstone County, Montana
Nebraska
The State of Nebraska comprises 93 counties.

Adams County, Nebraska
Antelope County, Nebraska
Arthur County, Nebraska
Banner County, Nebraska
Blaine County, Nebraska
Boone County, Nebraska
Box Butte County, Nebraska
Boyd County, Nebraska
Brown County, Nebraska
Buffalo County, Nebraska
Burt County, Nebraska
Butler County, Nebraska
Cass County, Nebraska
Cedar County, Nebraska
Chase County, Nebraska
Cherry County, Nebraska
Cheyenne County, Nebraska
Clay County, Nebraska
Colfax County, Nebraska
Cuming County, Nebraska
Custer County, Nebraska
Dakota County, Nebraska
Dawes County, Nebraska
Dawson County, Nebraska
Deuel County, Nebraska
Dixon County, Nebraska
Dodge County, Nebraska
Douglas County, Nebraska
Dundy County, Nebraska
Fillmore County, Nebraska
Franklin County, Nebraska
Frontier County, Nebraska
Furnas County, Nebraska
Gage County, Nebraska
Garden County, Nebraska
Garfield County, Nebraska
Gosper County, Nebraska
Grant County, Nebraska
Greeley County, Nebraska
Hall County, Nebraska
Hamilton County, Nebraska
Harlan County, Nebraska
Hayes County, Nebraska
Hitchcock County, Nebraska
Holt County, Nebraska
Hooker County, Nebraska
Howard County, Nebraska
Jefferson County, Nebraska
Johnson County, Nebraska
Kearney County, Nebraska
Keith County, Nebraska
Keya Paha County, Nebraska
Kimball County, Nebraska
Knox County, Nebraska
Lancaster County, Nebraska
Lincoln County, Nebraska
Logan County, Nebraska
Loup County, Nebraska
McPherson County, Nebraska
Madison County, Nebraska
Merrick County, Nebraska
Morrill County, Nebraska
Nance County, Nebraska
Nemaha County, Nebraska
Nuckolls County, Nebraska
Otoe County, Nebraska
Pawnee County, Nebraska
Perkins County, Nebraska
Phelps County, Nebraska
Pierce County, Nebraska
Platte County, Nebraska
Polk County, Nebraska
Red Willow County, Nebraska
Richardson County, Nebraska
Rock County, Nebraska
Saline County, Nebraska
Sarpy County, Nebraska
Saunders County, Nebraska
Scotts Bluff County, Nebraska
Seward County, Nebraska
Sheridan County, Nebraska
Sherman County, Nebraska
Sioux County, Nebraska
Stanton County, Nebraska
Thayer County, Nebraska
Thomas County, Nebraska
Thurston County, Nebraska
Valley County, Nebraska
Washington County, Nebraska
Wayne County, Nebraska
Webster County, Nebraska
Wheeler County, Nebraska
York County, Nebraska
Nevada
The State of Nevada comprises 16 counties and one independent city.

Carson City, Nevada
Churchill County, Nevada
Clark County, Nevada
Douglas County, Nevada
Elko County, Nevada
Esmeralda County, Nevada
Eureka County, Nevada
Humboldt County, Nevada
Lander County, Nevada
Lincoln County, Nevada
Lyon County, Nevada
Mineral County, Nevada
Nye County, Nevada
Pershing County, Nevada
Storey County, Nevada
Washoe County, Nevada
White Pine County, Nevada
New Hampshire
The State of New Hampshire comprises 10 counties.

Belknap County, New Hampshire
Carroll County, New Hampshire
Cheshire County, New Hampshire
Coos County, New Hampshire
Grafton County, New Hampshire
Hillsborough County, New Hampshire
Merrimack County, New Hampshire
Rockingham County, New Hampshire
Strafford County, New Hampshire
Sullivan County, New Hampshire
New Jersey
The State of New Jersey comprises 21 counties.

Atlantic County, New Jersey
Bergen County, New Jersey
Burlington County, New Jersey
Camden County, New Jersey
Cape May County, New Jersey
Cumberland County, New Jersey
Essex County, New Jersey
Gloucester County, New Jersey
Hudson County, New Jersey
Hunterdon County, New Jersey
Mercer County, New Jersey
Middlesex County, New Jersey
Monmouth County, New Jersey
Morris County, New Jersey
Ocean County, New Jersey
Passaic County, New Jersey
Salem County, New Jersey
Somerset County, New Jersey
Sussex County, New Jersey
Union County, New Jersey
Warren County, New Jersey
New Mexico
The State of New Mexico comprises 33 counties, including one consolidated city-county government.

Bernalillo County, New Mexico
Catron County, New Mexico
Chaves County, New Mexico
Cibola County, New Mexico
Colfax County, New Mexico
Curry County, New Mexico
De Baca County, New Mexico
Doña Ana County, New Mexico
Eddy County, New Mexico
Grant County, New Mexico
Guadalupe County, New Mexico
Harding County, New Mexico
Hidalgo County, New Mexico
Lea County, New Mexico
Lincoln County, New Mexico
Los Alamos County, New Mexico
Luna County, New Mexico
McKinley County, New Mexico
Mora County, New Mexico
Otero County, New Mexico
Quay County, New Mexico
Rio Arriba County, New Mexico
Roosevelt County, New Mexico
Sandoval County, New Mexico
San Juan County, New Mexico
San Miguel County, New Mexico
Santa Fe County, New Mexico
Sierra County, New Mexico
Socorro County, New Mexico
Taos County, New Mexico
Torrance County, New Mexico
Union County, New Mexico
Valencia County, New Mexico
New York
The State of New York comprises 62 counties.

Albany County, New York
Allegany County, New York
Bronx County, New York[32]
Broome County, New York
Cattaraugus County, New York
Cayuga County, New York
Chautauqua County, New York
Chemung County, New York
Chenango County, New York
Clinton County, New York
Columbia County, New York
Cortland County, New York
Delaware County, New York
Dutchess County, New York
Erie County, New York
Essex County, New York
Franklin County, New York
Fulton County, New York
Genesee County, New York
Greene County, New York
Hamilton County, New York
Herkimer County, New York
Jefferson County, New York
Kings County, New York[33]
Lewis County, New York
Livingston County, New York
Madison County, New York
Monroe County, New York
Montgomery County, New York
Nassau County, New York
New York County, New York[34]
Niagara County, New York
Oneida County, New York
Onondaga County, New York
Ontario County, New York
Orange County, New York
Orleans County, New York
Oswego County, New York
Otsego County, New York
Putnam County, New York
Queens County, New York[35]
Rensselaer County, New York
Richmond County, New York[36]
Rockland County, New York
Saint Lawrence County, New York
Saratoga County, New York
Schenectady County, New York
Schoharie County, New York
Schuyler County, New York
Seneca County, New York
Steuben County, New York
Suffolk County, New York
Sullivan County, New York
Tioga County, New York
Tompkins County, New York
Ulster County, New York
Warren County, New York
Washington County, New York
Wayne County, New York
Westchester County, New York
Wyoming County, New York
Yates County, New York
North Carolina
The State of North Carolina comprises 100 counties, including one consolidated city-county (Camden).

Alamance County, North Carolina
Alexander County, North Carolina
Alleghany County, North Carolina
Anson County, North Carolina
Ashe County, North Carolina
Avery County, North Carolina
Beaufort County, North Carolina
Bertie County, North Carolina
Bladen County, North Carolina
Brunswick County, North Carolina
Buncombe County, North Carolina
Burke County, North Carolina
Cabarrus County, North Carolina
Caldwell County, North Carolina
Camden County, North Carolina
Carteret County, North Carolina
Caswell County, North Carolina
Catawba County, North Carolina
Chatham County, North Carolina
Cherokee County, North Carolina
Chowan County, North Carolina
Clay County, North Carolina
Cleveland County, North Carolina
Columbus County, North Carolina
Craven County, North Carolina
Cumberland County, North Carolina
Currituck County, North Carolina
Dare County, North Carolina
Davidson County, North Carolina
Davie County, North Carolina
Duplin County, North Carolina
Durham County, North Carolina
Edgecombe County, North Carolina
Forsyth County, North Carolina
Franklin County, North Carolina
Gaston County, North Carolina
Gates County, North Carolina
Graham County, North Carolina
Granville County, North Carolina
Greene County, North Carolina
Guilford County, North Carolina
Halifax County, North Carolina
Harnett County, North Carolina
Haywood County, North Carolina
Henderson County, North Carolina
Hertford County, North Carolina
Hoke County, North Carolina
Hyde County, North Carolina
Iredell County, North Carolina
Jackson County, North Carolina
Johnston County, North Carolina
Jones County, North Carolina
Lee County, North Carolina
Lenoir County, North Carolina
Lincoln County, North Carolina
McDowell County, North Carolina
Macon County, North Carolina
Madison County, North Carolina
Martin County, North Carolina
Mecklenburg County, North Carolina
Mitchell County, North Carolina
Montgomery County, North Carolina
Moore County, North Carolina
Nash County, North Carolina
New Hanover County, North Carolina
Northampton County, North Carolina
Onslow County, North Carolina
Orange County, North Carolina
Pamlico County, North Carolina
Pasquotank County, North Carolina
Pender County, North Carolina
Perquimans County, North Carolina
Person County, North Carolina
Pitt County, North Carolina
Polk County, North Carolina
Randolph County, North Carolina
Richmond County, North Carolina
Robeson County, North Carolina
Rockingham County, North Carolina
Rowan County, North Carolina
Rutherford County, North Carolina
Sampson County, North Carolina
Scotland County, North Carolina
Stanly County, North Carolina
Stokes County, North Carolina
Surry County, North Carolina
Swain County, North Carolina
Transylvania County, North Carolina
Tyrrell County, North Carolina
Union County, North Carolina
Vance County, North Carolina
Wake County, North Carolina
Warren County, North Carolina
Washington County, North Carolina
Watauga County, North Carolina
Wayne County, North Carolina
Wilkes County, North Carolina
Wilson County, North Carolina
Yadkin County, North Carolina
Yancey County, North Carolina
North Dakota
The State of North Dakota comprises 53 counties.

Adams County, North Dakota
Barnes County, North Dakota
Benson County, North Dakota
Billings County, North Dakota
Bottineau County, North Dakota
Bowman County, North Dakota
Burke County, North Dakota
Burleigh County, North Dakota
Cass County, North Dakota
Cavalier County, North Dakota
Dickey County, North Dakota
Divide County, North Dakota
Dunn County, North Dakota
Eddy County, North Dakota
Emmons County, North Dakota
Foster County, North Dakota
Golden Valley County, North Dakota
Grand Forks County, North Dakota
Grant County, North Dakota
Griggs County, North Dakota
Hettinger County, North Dakota
Kidder County, North Dakota
LaMoure County, North Dakota
Logan County, North Dakota
McHenry County, North Dakota
McIntosh County, North Dakota
McKenzie County, North Dakota
McLean County, North Dakota
Mercer County, North Dakota
Morton County, North Dakota
Mountrail County, North Dakota
Nelson County, North Dakota
Oliver County, North Dakota
Pembina County, North Dakota
Pierce County, North Dakota
Ramsey County, North Dakota
Ransom County, North Dakota
Renville County, North Dakota
Richland County, North Dakota
Rolette County, North Dakota
Sargent County, North Dakota
Sheridan County, North Dakota
Sioux County, North Dakota
Slope County, North Dakota
Stark County, North Dakota
Steele County, North Dakota
Stutsman County, North Dakota
Towner County, North Dakota
Traill County, North Dakota
Walsh County, North Dakota
Ward County, North Dakota
Wells County, North Dakota
Williams County, North Dakota
Ohio
The State of Ohio comprises 88 counties.

Adams County, Ohio
Allen County, Ohio
Ashland County, Ohio
Ashtabula County, Ohio
Athens County, Ohio
Auglaize County, Ohio
Belmont County, Ohio
Brown County, Ohio
Butler County, Ohio
Carroll County, Ohio
Champaign County, Ohio
Clark County, Ohio
Clermont County, Ohio
Clinton County, Ohio
Columbiana County, Ohio
Coshocton County, Ohio
Crawford County, Ohio
Cuyahoga County, Ohio
Darke County, Ohio
Defiance County, Ohio
Delaware County, Ohio
Erie County, Ohio
Fairfield County, Ohio
Fayette County, Ohio
Franklin County, Ohio
Fulton County, Ohio
Gallia County, Ohio
Geauga County, Ohio
Greene County, Ohio
Guernsey County, Ohio
Hamilton County, Ohio
Hancock County, Ohio
Hardin County, Ohio
Harrison County, Ohio
Henry County, Ohio
Highland County, Ohio
Hocking County, Ohio
Holmes County, Ohio
Huron County, Ohio
Jackson County, Ohio
Jefferson County, Ohio
Knox County, Ohio
Lake County, Ohio
Lawrence County, Ohio
Licking County, Ohio
Logan County, Ohio
Lorain County, Ohio
Lucas County, Ohio
Madison County, Ohio
Mahoning County, Ohio
Marion County, Ohio
Medina County, Ohio
Meigs County, Ohio
Mercer County, Ohio
Miami County, Ohio
Monroe County, Ohio
Montgomery County, Ohio
Morgan County, Ohio
Morrow County, Ohio
Muskingum County, Ohio
Noble County, Ohio
Ottawa County, Ohio
Paulding County, Ohio
Perry County, Ohio
Pickaway County, Ohio
Pike County, Ohio
Portage County, Ohio
Preble County, Ohio
Putnam County, Ohio
Richland County, Ohio
Ross County, Ohio
Sandusky County, Ohio
Scioto County, Ohio
Seneca County, Ohio
Shelby County, Ohio
Stark County, Ohio
Summit County, Ohio
Trumbull County, Ohio
Tuscarawas County, Ohio
Union County, Ohio
Van Wert County, Ohio
Vinton County, Ohio
Warren County, Ohio
Washington County, Ohio
Wayne County, Ohio
Williams County, Ohio
Wood County, Ohio
Wyandot County, Ohio
Oklahoma
The State of Oklahoma comprises 77 counties.

Adair County, Oklahoma
Alfalfa County, Oklahoma
Atoka County, Oklahoma
Beaver County, Oklahoma
Beckham County, Oklahoma
Blaine County, Oklahoma
Bryan County, Oklahoma
Caddo County, Oklahoma
Canadian County, Oklahoma
Carter County, Oklahoma
Cherokee County, Oklahoma
Choctaw County, Oklahoma
Cimarron County, Oklahoma
Cleveland County, Oklahoma
Coal County, Oklahoma
Comanche County, Oklahoma
Cotton County, Oklahoma
Craig County, Oklahoma
Creek County, Oklahoma
Custer County, Oklahoma
Delaware County, Oklahoma
Dewey County, Oklahoma
Ellis County, Oklahoma
Garfield County, Oklahoma
Garvin County, Oklahoma
Grady County, Oklahoma
Grant County, Oklahoma
Greer County, Oklahoma
Harmon County, Oklahoma
Harper County, Oklahoma
Haskell County, Oklahoma
Hughes County, Oklahoma
Jackson County, Oklahoma
Jefferson County, Oklahoma
Johnston County, Oklahoma
Kay County, Oklahoma
Kingfisher County, Oklahoma
Kiowa County, Oklahoma
Latimer County, Oklahoma
Le Flore County, Oklahoma
Lincoln County, Oklahoma
Logan County, Oklahoma
Love County, Oklahoma
McClain County, Oklahoma
McCurtain County, Oklahoma
McIntosh County, Oklahoma
Major County, Oklahoma
Marshall County, Oklahoma
Mayes County, Oklahoma
Murray County, Oklahoma
Muskogee County, Oklahoma
Noble County, Oklahoma
Nowata County, Oklahoma
Okfuskee County, Oklahoma
Oklahoma County, Oklahoma
Okmulgee County, Oklahoma
Osage County, Oklahoma
Ottawa County, Oklahoma
Pawnee County, Oklahoma
Payne County, Oklahoma
Pittsburg County, Oklahoma
Pontotoc County, Oklahoma
Pottawatomie County, Oklahoma
Pushmataha County, Oklahoma
Roger Mills County, Oklahoma
Rogers County, Oklahoma
Seminole County, Oklahoma
Sequoyah County, Oklahoma
Stephens County, Oklahoma
Texas County, Oklahoma
Tillman County, Oklahoma
Tulsa County, Oklahoma
Wagoner County, Oklahoma
Washington County, Oklahoma
Washita County, Oklahoma
Woods County, Oklahoma
Woodward County, Oklahoma
Oregon
The State of Oregon comprises 36 counties.

Baker County, Oregon
Benton County, Oregon
Clackamas County, Oregon
Clatsop County, Oregon
Columbia County, Oregon
Coos County, Oregon
Crook County, Oregon
Curry County, Oregon
Deschutes County, Oregon
Douglas County, Oregon
Gilliam County, Oregon
Grant County, Oregon
Harney County, Oregon
Hood River County, Oregon
Jackson County, Oregon
Jefferson County, Oregon
Josephine County, Oregon
Klamath County, Oregon
Lake County, Oregon
Lane County, Oregon
Lincoln County, Oregon
Linn County, Oregon
Malheur County, Oregon
Marion County, Oregon
Morrow County, Oregon
Multnomah County, Oregon
Polk County, Oregon
Sherman County, Oregon
Tillamook County, Oregon
Umatilla County, Oregon
Union County, Oregon
Wallowa County, Oregon
Wasco County, Oregon
Washington County, Oregon
Wheeler County, Oregon
Yamhill County, Oregon
Pennsylvania
The Commonwealth of Pennsylvania comprises 67 counties, including one consolidated city-county government.

Adams County, Pennsylvania
Allegheny County, Pennsylvania
Armstrong County, Pennsylvania
Beaver County, Pennsylvania
Bedford County, Pennsylvania
Berks County, Pennsylvania
Blair County, Pennsylvania
Bradford County, Pennsylvania
Bucks County, Pennsylvania
Butler County, Pennsylvania
Cambria County, Pennsylvania
Cameron County, Pennsylvania
Carbon County, Pennsylvania
Centre County, Pennsylvania
Chester County, Pennsylvania
Clarion County, Pennsylvania
Clearfield County, Pennsylvania
Clinton County, Pennsylvania
Columbia County, Pennsylvania
Crawford County, Pennsylvania
Cumberland County, Pennsylvania
Dauphin County, Pennsylvania
Delaware County, Pennsylvania
Elk County, Pennsylvania
Erie County, Pennsylvania
Fayette County, Pennsylvania
Forest County, Pennsylvania
Franklin County, Pennsylvania
Fulton County, Pennsylvania
Greene County, Pennsylvania
Huntingdon County, Pennsylvania
Indiana County, Pennsylvania
Jefferson County, Pennsylvania
Juniata County, Pennsylvania
Lackawanna County, Pennsylvania
Lancaster County, Pennsylvania
Lawrence County, Pennsylvania
Lebanon County, Pennsylvania
Lehigh County, Pennsylvania
Luzerne County, Pennsylvania
Lycoming County, Pennsylvania
McKean County, Pennsylvania
Mercer County, Pennsylvania
Mifflin County, Pennsylvania
Monroe County, Pennsylvania
Montgomery County, Pennsylvania
Montour County, Pennsylvania
Northampton County, Pennsylvania
Northumberland County, Pennsylvania
Perry County, Pennsylvania
Philadelphia County, Pennsylvania[37]
Pike County, Pennsylvania
Potter County, Pennsylvania
Schuylkill County, Pennsylvania
Snyder County, Pennsylvania
Somerset County, Pennsylvania
Sullivan County, Pennsylvania
Susquehanna County, Pennsylvania
Tioga County, Pennsylvania
Union County, Pennsylvania
Venango County, Pennsylvania
Warren County, Pennsylvania
Washington County, Pennsylvania
Wayne County, Pennsylvania
Westmoreland County, Pennsylvania
Wyoming County, Pennsylvania
York County, Pennsylvania
Puerto Rico
The Commonwealth of Puerto Rico has no counties. The U.S. Census Bureau counts the 78 municipalities of Puerto Rico as county-equivalents.[1][2]

Adjuntas Municipality, Puerto Rico
Aguada Municipality, Puerto Rico
Aguadilla Municipality, Puerto Rico
Aguas Buenas Municipality, Puerto Rico
Aibonito Municipality, Puerto Rico
Añasco Municipality, Puerto Rico
Arecibo Municipality, Puerto Rico
Arroyo Municipality, Puerto Rico
Barceloneta Municipality, Puerto Rico
Barranquitas Municipality, Puerto Rico
Bayamón Municipality, Puerto Rico
Cabo Rojo Municipality, Puerto Rico
Caguas Municipality, Puerto Rico
Camuy Municipality, Puerto Rico
Canóvanas Municipality, Puerto Rico
Carolina Municipality, Puerto Rico
Cataño Municipality, Puerto Rico
Cayey Municipality, Puerto Rico
Ceiba Municipality, Puerto Rico
Ciales Municipality, Puerto Rico
Cidra Municipality, Puerto Rico
Coamo Municipality, Puerto Rico
Comerío Municipality, Puerto Rico
Corozal Municipality, Puerto Rico
Culebra Municipality, Puerto Rico
Dorado Municipality, Puerto Rico
Fajardo Municipality, Puerto Rico
Florida Municipality, Puerto Rico
Guánica Municipality, Puerto Rico
Guayama Municipality, Puerto Rico
Guayanilla Municipality, Puerto Rico
Guaynabo Municipality, Puerto Rico
Gurabo Municipality, Puerto Rico
Hatillo Municipality, Puerto Rico
Hormigueros Municipality, Puerto Rico
Humacao Municipality, Puerto Rico
Isabela Municipality, Puerto Rico
Jayuya Municipality, Puerto Rico
Juana Díaz Municipality, Puerto Rico
Juncos Municipality, Puerto Rico
Lajas Municipality, Puerto Rico
Lares Municipality, Puerto Rico
Las Marías Municipality, Puerto Rico
Las Piedras Municipality, Puerto Rico
Loíza Municipality, Puerto Rico
Luquillo Municipality, Puerto Rico
Manatí Municipality, Puerto Rico
Maricao Municipality, Puerto Rico
Maunabo Municipality, Puerto Rico
Mayagüez Municipality, Puerto Rico
Moca Municipality, Puerto Rico
Morovis Municipality, Puerto Rico
Naguabo Municipality, Puerto Rico
Naranjito Municipality, Puerto Rico
Orocovis Municipality, Puerto Rico
Patillas Municipality, Puerto Rico
Peñuelas Municipality, Puerto Rico
Ponce Municipality, Puerto Rico
Quebradillas Municipality, Puerto Rico
Rincón Municipality, Puerto Rico
Río Grande Municipality, Puerto Rico
Sabana Grande Municipality, Puerto Rico
Salinas Municipality, Puerto Rico
San Germán Municipality, Puerto Rico
San Juan Municipality, Puerto Rico
San Lorenzo Municipality, Puerto Rico
San Sebastián Municipality, Puerto Rico
Santa Isabel Municipality, Puerto Rico
Toa Alta Municipality, Puerto Rico
Toa Baja Municipality, Puerto Rico
Trujillo Alto Municipality, Puerto Rico
Utuado Municipality, Puerto Rico
Vega Alta Municipality, Puerto Rico
Vega Baja Municipality, Puerto Rico
Vieques Municipality, Puerto Rico
Villalba Municipality, Puerto Rico
Yabucoa Municipality, Puerto Rico
Yauco Municipality, Puerto Rico
Rhode Island
The State of Rhode Island and Providence Plantations comprises 5 counties.

Bristol County, Rhode Island
Kent County, Rhode Island
Newport County, Rhode Island
Providence County, Rhode Island
Washington County, Rhode Island
South Carolina
The State of South Carolina comprises 46 counties.

Abbeville County, South Carolina
Aiken County, South Carolina
Allendale County, South Carolina
Anderson County, South Carolina
Bamberg County, South Carolina
Barnwell County, South Carolina
Beaufort County, South Carolina
Berkeley County, South Carolina
Calhoun County, South Carolina
Charleston County, South Carolina
Cherokee County, South Carolina
Chester County, South Carolina
Chesterfield County, South Carolina
Clarendon County, South Carolina
Colleton County, South Carolina
Darlington County, South Carolina
Dillon County, South Carolina
Dorchester County, South Carolina
Edgefield County, South Carolina
Fairfield County, South Carolina
Florence County, South Carolina
Georgetown County, South Carolina
Greenville County, South Carolina
Greenwood County, South Carolina
Hampton County, South Carolina
Horry County, South Carolina
Jasper County, South Carolina
Kershaw County, South Carolina
Lancaster County, South Carolina
Laurens County, South Carolina
Lee County, South Carolina
Lexington County, South Carolina
McCormick County, South Carolina
Marion County, South Carolina
Marlboro County, South Carolina
Newberry County, South Carolina
Oconee County, South Carolina
Orangeburg County, South Carolina
Pickens County, South Carolina
Richland County, South Carolina
Saluda County, South Carolina
Spartanburg County, South Carolina
Sumter County, South Carolina
Union County, South Carolina
Williamsburg County, South Carolina
York County, South Carolina
South Dakota
The State of South Dakota comprises 66 counties.

Aurora County, South Dakota
Beadle County, South Dakota
Bennett County, South Dakota
Bon Homme County, South Dakota
Brookings County, South Dakota
Brown County, South Dakota
Brule County, South Dakota
Buffalo County, South Dakota
Butte County, South Dakota
Campbell County, South Dakota
Charles Mix County, South Dakota
Clark County, South Dakota
Clay County, South Dakota
Codington County, South Dakota
Corson County, South Dakota
Custer County, South Dakota
Davison County, South Dakota
Day County, South Dakota
Deuel County, South Dakota
Dewey County, South Dakota
Douglas County, South Dakota
Edmunds County, South Dakota
Fall River County, South Dakota
Faulk County, South Dakota
Grant County, South Dakota
Gregory County, South Dakota
Haakon County, South Dakota
Hamlin County, South Dakota
Hand County, South Dakota
Hanson County, South Dakota
Harding County, South Dakota
Hughes County, South Dakota
Hutchinson County, South Dakota
Hyde County, South Dakota
Jackson County, South Dakota
Jerauld County, South Dakota
Jones County, South Dakota
Kingsbury County, South Dakota
Lake County, South Dakota
Lawrence County, South Dakota
Lincoln County, South Dakota
Lyman County, South Dakota
McCook County, South Dakota
McPherson County, South Dakota
Marshall County, South Dakota
Meade County, South Dakota
Mellette County, South Dakota
Miner County, South Dakota
Minnehaha County, South Dakota
Moody County, South Dakota
Oglala Lakota County, South Dakota
Pennington County, South Dakota
Perkins County, South Dakota
Potter County, South Dakota
Roberts County, South Dakota
Sanborn County, South Dakota
Spink County, South Dakota
Stanley County, South Dakota
Sully County, South Dakota
Todd County, South Dakota
Tripp County, South Dakota
Turner County, South Dakota
Union County, South Dakota
Walworth County, South Dakota
Yankton County, South Dakota
Ziebach County, South Dakota
Tennessee
The State of Tennessee comprises 95 counties.

Anderson County, Tennessee
Bedford County, Tennessee
Benton County, Tennessee
Bledsoe County, Tennessee
Blount County, Tennessee
Bradley County, Tennessee
Campbell County, Tennessee
Cannon County, Tennessee
Carroll County, Tennessee
Carter County, Tennessee
Cheatham County, Tennessee
Chester County, Tennessee
Claiborne County, Tennessee
Clay County, Tennessee
Cocke County, Tennessee
Coffee County, Tennessee
Crockett County, Tennessee
Cumberland County, Tennessee
Davidson County, Tennessee[38]
Decatur County, Tennessee
DeKalb County, Tennessee
Dickson County, Tennessee
Dyer County, Tennessee
Fayette County, Tennessee
Fentress County, Tennessee
Franklin County, Tennessee
Gibson County, Tennessee
Giles County, Tennessee
Grainger County, Tennessee
Greene County, Tennessee
Grundy County, Tennessee
Hamblen County, Tennessee
Hamilton County, Tennessee
Hancock County, Tennessee
Hardeman County, Tennessee
Hardin County, Tennessee
Hawkins County, Tennessee
Haywood County, Tennessee
Henderson County, Tennessee
Henry County, Tennessee
Hickman County, Tennessee
Houston County, Tennessee
Humphreys County, Tennessee
Jackson County, Tennessee
Jefferson County, Tennessee
Johnson County, Tennessee
Knox County, Tennessee
Lake County, Tennessee
Lauderdale County, Tennessee
Lawrence County, Tennessee
Lewis County, Tennessee
Lincoln County, Tennessee
Loudon County, Tennessee
McMinn County, Tennessee
McNairy County, Tennessee
Macon County, Tennessee
Madison County, Tennessee
Marion County, Tennessee
Marshall County, Tennessee
Maury County, Tennessee
Meigs County, Tennessee
Monroe County, Tennessee
Montgomery County, Tennessee
Moore County, Tennessee[39]
Morgan County, Tennessee
Obion County, Tennessee
Overton County, Tennessee
Perry County, Tennessee
Pickett County, Tennessee
Polk County, Tennessee
Putnam County, Tennessee
Rhea County, Tennessee
Roane County, Tennessee
Robertson County, Tennessee
Rutherford County, Tennessee
Scott County, Tennessee
Sequatchie County, Tennessee
Sevier County, Tennessee
Shelby County, Tennessee
Smith County, Tennessee
Stewart County, Tennessee
Sullivan County, Tennessee
Sumner County, Tennessee
Tipton County, Tennessee
Trousdale County, Tennessee[40]
Unicoi County, Tennessee
Union County, Tennessee
Van Buren County, Tennessee
Warren County, Tennessee
Washington County, Tennessee
Wayne County, Tennessee
Weakley County, Tennessee
White County, Tennessee
Williamson County, Tennessee
Wilson County, Tennessee
Texas
The State of Texas comprises 254 counties.

Anderson County, Texas
Andrews County, Texas
Angelina County, Texas
Aransas County, Texas
Archer County, Texas
Armstrong County, Texas
Atascosa County, Texas
Austin County, Texas
Bailey County, Texas
Bandera County, Texas
Bastrop County, Texas
Baylor County, Texas
Bee County, Texas
Bell County, Texas
Bexar County, Texas
Blanco County, Texas
Borden County, Texas
Bosque County, Texas
Bowie County, Texas
Brazoria County, Texas
Brazos County, Texas
Brewster County, Texas
Briscoe County, Texas
Brooks County, Texas
Brown County, Texas
Burleson County, Texas
Burnet County, Texas
Caldwell County, Texas
Calhoun County, Texas
Callahan County, Texas
Cameron County, Texas
Camp County, Texas
Carson County, Texas
Cass County, Texas
Castro County, Texas
Chambers County, Texas
Cherokee County, Texas
Childress County, Texas
Clay County, Texas
Cochran County, Texas
Coke County, Texas
Coleman County, Texas
Collin County, Texas
Collingsworth County, Texas
Colorado County, Texas
Comal County, Texas
Comanche County, Texas
Concho County, Texas
Cooke County, Texas
Coryell County, Texas
Cottle County, Texas
Crane County, Texas
Crockett County, Texas
Crosby County, Texas
Culberson County, Texas
Dallam County, Texas
Dallas County, Texas
Dawson County, Texas
Deaf Smith County, Texas
Delta County, Texas
Denton County, Texas
DeWitt County, Texas
Dickens County, Texas
Dimmit County, Texas
Donley County, Texas
Duval County, Texas
Eastland County, Texas
Ector County, Texas
Edwards County, Texas
Ellis County, Texas
El Paso County, Texas
Erath County, Texas
Falls County, Texas
Fannin County, Texas
Fayette County, Texas
Fisher County, Texas
Floyd County, Texas
Foard County, Texas
Fort Bend County, Texas
Franklin County, Texas
Freestone County, Texas
Frio County, Texas
Gaines County, Texas
Galveston County, Texas
Garza County, Texas
Gillespie County, Texas
Glasscock County, Texas
Goliad County, Texas
Gonzales County, Texas
Gray County, Texas
Grayson County, Texas
Gregg County, Texas
Grimes County, Texas
Guadalupe County, Texas
Hale County, Texas
Hall County, Texas
Hamilton County, Texas
Hansford County, Texas
Hardeman County, Texas
Hardin County, Texas
Harris County, Texas
Harrison County, Texas
Hartley County, Texas
Haskell County, Texas
Hays County, Texas
Hemphill County, Texas
Henderson County, Texas
Hidalgo County, Texas
Hill County, Texas
Hockley County, Texas
Hood County, Texas
Hopkins County, Texas
Houston County, Texas
Howard County, Texas
Hudspeth County, Texas
Hunt County, Texas
Hutchinson County, Texas
Irion County, Texas
Jack County, Texas
Jackson County, Texas
Jasper County, Texas
Jeff Davis County, Texas
Jefferson County, Texas
Jim Hogg County, Texas
Jim Wells County, Texas
Johnson County, Texas
Jones County, Texas
Karnes County, Texas
Kaufman County, Texas
Kendall County, Texas
Kenedy County, Texas
Kent County, Texas
Kerr County, Texas
Kimble County, Texas
King County, Texas
Kinney County, Texas
Kleberg County, Texas
Knox County, Texas
Lamar County, Texas
Lamb County, Texas
Lampasas County, Texas
LaSalle County, Texas
Lavaca County, Texas
Lee County, Texas
Leon County, Texas
Liberty County, Texas
Limestone County, Texas
Lipscomb County, Texas
Live Oak County, Texas
Llano County, Texas
Loving County, Texas
Lubbock County, Texas
Lynn County, Texas
McCulloch County, Texas
McLennan County, Texas
McMullen County, Texas
Madison County, Texas
Marion County, Texas
Martin County, Texas
Mason County, Texas
Matagorda County, Texas
Maverick County, Texas
Medina County, Texas
Menard County, Texas
Midland County, Texas
Milam County, Texas
Mills County, Texas
Mitchell County, Texas
Montague County, Texas
Montgomery County, Texas
Moore County, Texas
Morris County, Texas
Motley County, Texas
Nacogdoches County, Texas
Navarro County, Texas
Newton County, Texas
Nolan County, Texas
Nueces County, Texas
Ochiltree County, Texas
Oldham County, Texas
Orange County, Texas
Palo Pinto County, Texas
Panola County, Texas
Parker County, Texas
Parmer County, Texas
Pecos County, Texas
Polk County, Texas
Potter County, Texas
Presidio County, Texas
Rains County, Texas
Randall County, Texas
Reagan County, Texas
Real County, Texas
Red River County, Texas
Reeves County, Texas
Refugio County, Texas
Roberts County, Texas
Robertson County, Texas
Rockwall County, Texas
Runnels County, Texas
Rusk County, Texas
Sabine County, Texas
San Augustine County, Texas
San Jacinto County, Texas
San Patricio County, Texas
San Saba County, Texas
Schleicher County, Texas
Scurry County, Texas
Shackelford County, Texas
Shelby County, Texas
Sherman County, Texas
Smith County, Texas
Somervell County, Texas
Starr County, Texas
Stephens County, Texas
Sterling County, Texas
Stonewall County, Texas
Sutton County, Texas
Swisher County, Texas
Tarrant County, Texas
Taylor County, Texas
Terrell County, Texas
Terry County, Texas
Throckmorton County, Texas
Titus County, Texas
Tom Green County, Texas
Travis County, Texas
Trinity County, Texas
Tyler County, Texas
Upshur County, Texas
Upton County, Texas
Uvalde County, Texas
Val Verde County, Texas
Van Zandt County, Texas
Victoria County, Texas
Walker County, Texas
Waller County, Texas
Ward County, Texas
Washington County, Texas
Webb County, Texas
Wharton County, Texas
Wheeler County, Texas
Wichita County, Texas
Wilbarger County, Texas
Willacy County, Texas
Williamson County, Texas
Wilson County, Texas
Winkler County, Texas
Wise County, Texas
Wood County, Texas
Yoakum County, Texas
Young County, Texas
Zapata County, Texas
Zavala County, Texas
Utah
The State of Utah comprises 29 counties.

Beaver County, Utah
Box Elder County, Utah
Cache County, Utah
Carbon County, Utah
Daggett County, Utah
Davis County, Utah
Duchesne County, Utah
Emery County, Utah
Garfield County, Utah
Grand County, Utah
Iron County, Utah
Juab County, Utah
Kane County, Utah
Millard County, Utah
Morgan County, Utah
Piute County, Utah
Rich County, Utah
Salt Lake County, Utah
San Juan County, Utah
Sanpete County, Utah
Sevier County, Utah
Summit County, Utah
Tooele County, Utah
Uintah County, Utah
Utah County, Utah
Wasatch County, Utah
Washington County, Utah
Wayne County, Utah
Weber County, Utah
Vermont
The State of Vermont comprises 14 counties.

Addison County, Vermont
Bennington County, Vermont
Caledonia County, Vermont
Chittenden County, Vermont
Essex County, Vermont
Franklin County, Vermont
Grand Isle County, Vermont
Lamoille County, Vermont
Orange County, Vermont
Orleans County, Vermont
Rutland County, Vermont
Washington County, Vermont
Windham County, Vermont
Windsor County, Vermont
Virgin Islands (USA)
The Virgin Islands of the United States have no counties. The U.S. Census Bureau counts the 3 main islands of the U.S. Virgin Islands as county-equivalents.[1][2]

Saint Croix Island, U.S. Virgin Islands
Saint John Island, U.S. Virgin Islands
Saint Thomas Island, U.S. Virgin Islands
Virginia
The Commonwealth of Virginia comprises 95 counties and 38 independent cities.

Accomack County, Virginia
Albemarle County, Virginia
Alleghany County, Virginia
Amelia County, Virginia
Amherst County, Virginia
Appomattox County, Virginia
Arlington County, Virginia
Augusta County, Virginia
Bath County, Virginia
Bedford County, Virginia
Bland County, Virginia
Botetourt County, Virginia
Brunswick County, Virginia
Buchanan County, Virginia
Buckingham County, Virginia
Campbell County, Virginia
Caroline County, Virginia
Carroll County, Virginia
Charles City County, Virginia
Charlotte County, Virginia
Chesterfield County, Virginia
Clarke County, Virginia
Craig County, Virginia
Culpeper County, Virginia
Cumberland County, Virginia
Dickenson County, Virginia
Dinwiddie County, Virginia
Essex County, Virginia
Fairfax County, Virginia
Fauquier County, Virginia
Floyd County, Virginia
Fluvanna County, Virginia
Franklin County, Virginia
Frederick County, Virginia
Giles County, Virginia
Gloucester County, Virginia
Goochland County, Virginia
Grayson County, Virginia
Greene County, Virginia
Greensville County, Virginia
Halifax County, Virginia
Hanover County, Virginia
Henrico County, Virginia
Henry County, Virginia
Highland County, Virginia
Isle of Wight County, Virginia
James City County, Virginia
King and Queen County, Virginia
King George County, Virginia
King William County, Virginia
Lancaster County, Virginia
Lee County, Virginia
Loudoun County, Virginia
Louisa County, Virginia
Lunenburg County, Virginia
Madison County, Virginia
Mathews County, Virginia
Mecklenburg County, Virginia
Middlesex County, Virginia
Montgomery County, Virginia
Nelson County, Virginia
New Kent County, Virginia
Northampton County, Virginia
Northumberland County, Virginia
Nottoway County, Virginia
Orange County, Virginia
Page County, Virginia
Patrick County, Virginia
Pittsylvania County, Virginia
Powhatan County, Virginia
Prince Edward County, Virginia
Prince George County, Virginia
Prince William County, Virginia
Pulaski County, Virginia
Rappahannock County, Virginia
Richmond County, Virginia
Roanoke County, Virginia
Rockbridge County, Virginia
Rockingham County, Virginia
Russell County, Virginia
Scott County, Virginia
Shenandoah County, Virginia
Smyth County, Virginia
Southampton County, Virginia
Spotsylvania County, Virginia
Stafford County, Virginia
Surry County, Virginia
Sussex County, Virginia
Tazewell County, Virginia
Warren County, Virginia
Washington County, Virginia
Westmoreland County, Virginia
Wise County, Virginia
Wythe County, Virginia
York County, Virginia
City of Alexandria, Virginia[41]
City of Bristol, Virginia[41]
City of Buena Vista, Virginia[41]
City of Charlottesville, Virginia[41]
City of Chesapeake, Virginia[41]
City of Colonial Heights, Virginia[41]
City of Covington, Virginia[41]
City of Danville, Virginia[41]
City of Emporia, Virginia[41]
City of Fairfax, Virginia[41]
City of Falls Church, Virginia[41]
City of Franklin, Virginia[41]
City of Fredericksburg, Virginia[41]
City of Galax, Virginia[41]
City of Hampton, Virginia[41]
City of Harrisonburg, Virginia[41]
City of Hopewell, Virginia[41]
City of Lexington, Virginia[41]
City of Lynchburg, Virginia[41]
City of Manassas, Virginia[41]
City of Manassas Park, Virginia[41]
City of Martinsville, Virginia[41]
City of Newport News, Virginia[41]
City of Norfolk, Virginia[41]
City of Norton, Virginia[41]
City of Petersburg, Virginia[41]
City of Poquoson, Virginia[41]
City of Portsmouth, Virginia[41]
City of Radford, Virginia[41]
City of Richmond, Virginia[41]
City of Roanoke, Virginia[41]
City of Salem, Virginia[41]
City of Staunton, Virginia[41]
City of Suffolk, Virginia[41]
City of Virginia Beach, Virginia[41]
City of Waynesboro, Virginia[41]
City of Williamsburg, Virginia[41]
City of Winchester, Virginia[41]
Washington
The State of Washington comprises 39 counties.

Adams County, Washington
Asotin County, Washington
Benton County, Washington
Chelan County, Washington
Clallam County, Washington
Clark County, Washington
Columbia County, Washington
Cowlitz County, Washington
Douglas County, Washington
Ferry County, Washington
Franklin County, Washington
Garfield County, Washington
Grant County, Washington
Grays Harbor County, Washington
Island County, Washington
Jefferson County, Washington
King County, Washington
Kitsap County, Washington
Kittitas County, Washington
Klickitat County, Washington
Lewis County, Washington
Lincoln County, Washington
Mason County, Washington
Okanogan County, Washington
Pacific County, Washington
Pend Oreille County, Washington
Pierce County, Washington
San Juan County, Washington
Skagit County, Washington
Skamania County, Washington
Snohomish County, Washington
Spokane County, Washington
Stevens County, Washington
Thurston County, Washington
Wahkiakum County, Washington
Walla Walla County, Washington
Whatcom County, Washington
Whitman County, Washington
Yakima County, Washington
West Virginia
The State of West Virginia comprises 55 counties.

Barbour County, West Virginia
Berkeley County, West Virginia
Boone County, West Virginia
Braxton County, West Virginia
Brooke County, West Virginia
Cabell County, West Virginia
Calhoun County, West Virginia
Clay County, West Virginia
Doddridge County, West Virginia
Fayette County, West Virginia
Gilmer County, West Virginia
Grant County, West Virginia
Greenbrier County, West Virginia
Hampshire County, West Virginia
Hancock County, West Virginia
Hardy County, West Virginia
Harrison County, West Virginia
Jackson County, West Virginia
Jefferson County, West Virginia
Kanawha County, West Virginia
Lewis County, West Virginia
Lincoln County, West Virginia
Logan County, West Virginia
McDowell County, West Virginia
Marion County, West Virginia
Marshall County, West Virginia
Mason County, West Virginia
Mercer County, West Virginia
Mineral County, West Virginia
Mingo County, West Virginia
Monongalia County, West Virginia
Monroe County, West Virginia
Morgan County, West Virginia
Nicholas County, West Virginia
Ohio County, West Virginia
Pendleton County, West Virginia
Pleasants County, West Virginia
Pocahontas County, West Virginia
Preston County, West Virginia
Putnam County, West Virginia
Raleigh County, West Virginia
Randolph County, West Virginia
Ritchie County, West Virginia
Roane County, West Virginia
Summers County, West Virginia
Taylor County, West Virginia
Tucker County, West Virginia
Tyler County, West Virginia
Upshur County, West Virginia
Wayne County, West Virginia
Webster County, West Virginia
Wetzel County, West Virginia
Wirt County, West Virginia
Wood County, West Virginia
Wyoming County, West Virginia
Wisconsin
The State of Wisconsin comprises 72 counties.

Adams County, Wisconsin
Ashland County, Wisconsin
Barron County, Wisconsin
Bayfield County, Wisconsin
Brown County, Wisconsin
Buffalo County, Wisconsin
Burnett County, Wisconsin
Calumet County, Wisconsin
Chippewa County, Wisconsin
Clark County, Wisconsin
Columbia County, Wisconsin
Crawford County, Wisconsin
Dane County, Wisconsin
Dodge County, Wisconsin
Door County, Wisconsin
Douglas County, Wisconsin
Dunn County, Wisconsin
Eau Claire County, Wisconsin
Florence County, Wisconsin
Fond du Lac County, Wisconsin
Forest County, Wisconsin
Grant County, Wisconsin
Green County, Wisconsin
Green Lake County, Wisconsin
Iowa County, Wisconsin
Iron County, Wisconsin
Jackson County, Wisconsin
Jefferson County, Wisconsin
Juneau County, Wisconsin
Kenosha County, Wisconsin
Kewaunee County, Wisconsin
La Crosse County, Wisconsin
Lafayette County, Wisconsin
Langlade County, Wisconsin
Lincoln County, Wisconsin
Manitowoc County, Wisconsin
Marathon County, Wisconsin
Marinette County, Wisconsin
Marquette County, Wisconsin
Menominee County, Wisconsin
Milwaukee County, Wisconsin
Monroe County, Wisconsin
Oconto County, Wisconsin
Oneida County, Wisconsin
Outagamie County, Wisconsin
Ozaukee County, Wisconsin
Pepin County, Wisconsin
Pierce County, Wisconsin
Polk County, Wisconsin
Portage County, Wisconsin
Price County, Wisconsin
Racine County, Wisconsin
Richland County, Wisconsin
Rock County, Wisconsin
Rusk County, Wisconsin
Saint Croix County, Wisconsin
Sauk County, Wisconsin
Sawyer County, Wisconsin
Shawano County, Wisconsin
Sheboygan County, Wisconsin
Taylor County, Wisconsin
Trempealeau County, Wisconsin
Vernon County, Wisconsin
Vilas County, Wisconsin
Walworth County, Wisconsin
Washburn County, Wisconsin
Washington County, Wisconsin
Waukesha County, Wisconsin
Waupaca County, Wisconsin
Waushara County, Wisconsin
Winnebago County, Wisconsin
Wood County, Wisconsin
Wyoming
The State of Wyoming comprises 23 counties.

Albany County, Wyoming
Big Horn County, Wyoming
Campbell County, Wyoming
Carbon County, Wyoming
Converse County, Wyoming
Crook County, Wyoming
Fremont County, Wyoming
Goshen County, Wyoming
Hot Springs County, Wyoming
Johnson County, Wyoming
Laramie County, Wyoming
Lincoln County, Wyoming
Natrona County, Wyoming
Niobrara County, Wyoming
Park County, Wyoming
Platte County, Wyoming
Sheridan County, Wyoming
Sublette County, Wyoming
Sweetwater County, Wyoming
Teton County, Wyoming
Uinta County, Wyoming
Washakie County, Wyoming
Weston County, Wyoming"""

def reject(line):
    return ( len(line) == 0 or                \
             "The State of" in line or        \
             "The Commonwealth of" in line or \
             "City of" in line or             \
             "Virgin Is" in line or           \
             "Puerto Rico" in line or         \
             "Guam" in line or                \
             "American Samoa" in line or      \
             "District of Columbia" in line
           )

pass_one = []
for line in data.split("\n"):
    if not reject(line):
        fields = line.split()
        if "," in line:
            pass_one.append("    " + line.split("[")[0])
        else:
            pass_one.append(line)

states = defaultdict(list)
current_state = None
for line in pass_one:
    if not line.startswith(" "):
        current_state = line
    else:
        states[current_state].append(line.lstrip().split(",")[0])

with open("counties.json","w") as fp:
    output_data = json.dumps(states, indent=2)
    fp.write(output_data)
        

