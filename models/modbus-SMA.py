# Supported hardware and firmware:
# Sunny Boy 3.0 / 3.6 / 4.0 / 5.0
# Sunny Boy: SB3.0-1AV-40 / SB3.6-1AV-40 / SB4.0-1AV-40 / SB5.0-1AV-40
# Starting with software package: 01.03.04.R


# Full list of readable registers - comment out registers you aren't interested in for faster performance
#
# Descriptions generated by using the following formula in SMA_Modbus-TI-en-26.xlsx - available from SMA web site
#   ="  ['"&A3&" - "&IFERROR(LEFT(B3,FIND(":",B3)-1),B3)&IF(C3<>""," ("&C3&")","")&"',"&A3&",'"&D3&"','"&E3&"'],"
#
# Note: The following manual updates were made:
#       * Updates from STR32 to STR16 as the SMA doco appears to be wrong for 31017, 31025, 31033, 31041, 40159, 40167, 40175 and 40513
#       * Remove extended characters from temperatures in 30953, 34109 and 34113
#       * Comment out write only registers: 40015, 40016, 40018, 40022, 40023, 40024, 40025 and 40999

sma_registers = [
#  ['30051 - Device class',30051,'U32','ENUM'],
#  ['30053 - Device type',30053,'U32','ENUM'],
#  ['30057 - Serial number',30057,'U32','RAW'],
#  ['30059 - Software package',30059,'U32','FW'],
#  ['30199 - Waiting time until feed-in (s)',30199,'U32','Duration'],
#  ['30201 - Condition',30201,'U32','ENUM'],
#  ['30203 - Nominal power in Ok Mode (W)',30203,'U32','FIX0'],
#  ['30205 - Nominal power in Warning Mode (W)',30205,'U32','FIX0'],
#  ['30207 - Nominal power in Fault Mode (W)',30207,'U32','FIX0'],
#  ['30211 - Recommended action',30211,'U32','ENUM'],
#  ['30213 - Message',30213,'U32','ENUM'],
#  ['30215 - Fault correction measure',30215,'U32','ENUM'],
#  ['30217 - Grid relay/contactor',30217,'U32','ENUM'],
#  ['30225 - Insulation resistance (Ohms)',30225,'U32','FIX0'],
#  ['30231 - Maximum active power device (W)',30231,'U32','FIX0'],
#  ['30233 - Set active power limit (W)',30233,'U32','FIX0'],
#  ['30247 - Current event number for manufacturer',30247,'U32','FIX0'],
#  ['30513 - Total yield (Wh)',30513,'U64','FIX0'],
#  ['30517 - Daily yield (Wh)',30517,'U64','FIX0'],
#  ['30521 - Operating time (s)',30521,'U64','Duration'],
#  ['30525 - Feed-in time (s)',30525,'U64','Duration'],
#  ['30529 - Total yield (Wh)',30529,'U32','FIX0'],
#  ['30531 - Total yield (kWh)',30531,'U32','FIX0'],
#  ['30533 - Total yield (MWh)',30533,'U32','FIX0'],
  ['daily_power_yield',30535,'U32','FIX0'],
#  ['30537 - Daily yield (kWh)',30537,'U32','FIX0'],
#  ['30539 - Daily yield (MWh)',30539,'U32','FIX0'],
#  ['30541 - Operating time (s)',30541,'U32','Duration'],
#  ['30543 - Feed-in time (s)',30543,'U32','Duration'],
#  ['30559 - Number of events for user',30559,'U32','FIX0'],
#  ['30561 - Number of events for installer',30561,'U32','FIX0'],
#  ['30563 - Number of events for service',30563,'U32','FIX0'],
#  ['30581 - Grid reference counter reading (Wh)',30581,'U32','FIX0'],
#  ['30583 - Grid feed-in counter reading (Wh)',30583,'U32','FIX0'],
#  ['30599 - Number of grid connections',30599,'U32','FIX0'],
#  ['30769 - DC current input [1] (A)',30769,'S32','FIX3'],
#  ['30771 - DC voltage input [1] (V)',30771,'S32','FIX2'],
#  ['30773 - DC power input [1] (W)',30773,'S32','FIX0'],
  ['total_pv_power',30775,'S32','FIX0'],
#  ['30783 - Grid voltage phase L1 (V)',30783,'U32','FIX2'],
#  ['30785 - Grid voltage phase L2 (V)',30785,'U32','FIX2'],
#  ['30787 - Grid voltage phase L3 (V)',30787,'U32','FIX2'],
#  ['30803 - Grid frequency (Hz)',30803,'U32','FIX2'],
#  ['30805 - Reactive power (VAr)',30805,'S32','FIX0'],
#  ['30813 - Apparent power (VA)',30813,'S32','FIX0'],
#  ['30823 - Excitation type of cosPhi',30823,'U32','ENUM'],
#  ['30825 - Operating mode of stat.V stab., stat.V stab. config.',30825,'U32','ENUM'],
#  ['30829 - Reactive power set value as a % (%)',30829,'S32','FIX1'],
#  ['30831 - cosPhi setpoint, cosPhi config., direct specif.',30831,'S32','FIX2'],
#  ['30833 - cosPhi excit.type, cosPhi config., direct spec.',30833,'U32','ENUM'],
#  ['30835 - Operating mode of feed-in management',30835,'U32','ENUM'],
#  ['30837 - Active power limitation P, active power configuration (W)',30837,'U32','FIX0'],
#  ['30839 - Active power limitation P, active power configuration (%)',30839,'U32','FIX0'],
#  ['30865 - Power grid reference (W)',30865,'S32','FIX0'],
#  ['30867 - Power grid feed-in (W)',30867,'S32','FIX0'],
#  ['30925 - Connection speed of SMACOM A',30925,'U32','ENUM'],
#  ['30927 - Duplex mode of SMACOM A',30927,'U32','ENUM'],
#  ['30929 - Speedwire connection status of SMACOM A',30929,'U32','ENUM'],
#  ['30949 - Displacement power factor ',30949,'U32','FIX3'],
  ['internal_temp',30953,'S32','TEMP'] #'30953 - Internal temperature (C)'
#  ['30957 - DC current input [2] (A)',30957,'S32','FIX3'],
#  ['30959 - DC voltage input [2] (V)',30959,'S32','FIX2'],
#  ['30961 - DC power input [2] (W)',30961,'S32','FIX0'],
#  ['30975 - Intermediate circuit voltage (V)',30975,'S32','FIX2'],
#  ['30977 - Grid current phase L1 (A)',30977,'S32','FIX3'],
#  ['30979 - Grid current phase L2 (A)',30979,'S32','FIX3'],
#  ['30981 - Grid current phase L3 (A)',30981,'S32','FIX3'],
#  ['31017 - Current speedwire IP address',31017,'STR16','UTF8'],
#  ['31025 - Current speedwire subnet mask',31025,'STR16','UTF8'],
#  ['31033 - Current speedwire gateway address',31033,'STR16','UTF8'],
#  ['31041 - Current speedwire DNS server address',31041,'STR16','UTF8'],
#  ['31085 - Nominal power in Ok Mode (W)',31085,'U32','FIX0'],
#  ['31247 - Residual current (A)',31247,'S32','FIX3'],
#  ['34109 - Heat sink temperature (C)',34109,'S32','TEMP'],
#  ['34113 - Internal temperature (C)',34113,'S32','TEMP'],
#  ['35377 - Number of events for user',35377,'U64','FIX0'],
#  ['35381 - Number of events for installer',35381,'U64','FIX0'],
#  ['35385 - Number of events for service',35385,'U64','FIX0'],
#  ['40003 - Time zone',40003,'U32','ENUM'],
#  ['40005 - Standard/Daylight saving time conversion on',40005,'U32','ENUM'],
#  ['40009 - Operating condition',40009,'U32','ENUM'],
#  ['40013 - Language of the user interface',40013,'U32','ENUM'],
#  ['40015 - Normalized reactive power limitation by PV system ctrl (%)',40015,'S16','FIX1'], # Write only
#  ['40016 - Normalized active power limitation by PV system ctrl (%)',40016,'S16','FIX0'], # Write only
#  ['40018 - Fast shut-down',40018,'U32','ENUM'], # Write only
#  ['40022 - Normalized reactive power limitation by PV system ctrl (%)',40022,'S16','FIX2'], # Write only
#  ['40023 - Normalized active power limitation by PV system ctrl (%)',40023,'S16','FIX2'], # Write only
#  ['40024 - Dis.pow.factor that can be changed via PV system ctrl',40024,'U16','FIX4'], # Write only
#  ['40025 - Excitation type that can be changed by PV system ctrl',40025,'U32','ENUM'], # Write only
#  ['40063 - Firmware version of the main processor',40063,'U32','FW'],
#  ['40067 - Serial number',40067,'U32','RAW'],
#  ['40109 - Country standard set',40109,'U32','ENUM'],
#  ['40133 - Grid nominal voltage (V)',40133,'U32','FIX0'],
#  ['40135 - Nominal frequency (Hz)',40135,'U32','FIX2'],
#  ['40157 - Automatic speedwire configureation switched on',40157,'U32','ENUM'],
#  ['40159 - Speedwire IP address',40159,'STR16','IP4'],
#  ['40167 - Speedwire subnet mask',40167,'STR16','IP4'],
#  ['40175 - Speedwire gateway address',40175,'STR16','IP4'],
#  ['40183 - Phase assignment',40183,'U32','ENUM'],
#  ['40185 - Maximum apparent power device (VA)',40185,'U32','FIX0'],
#  ['40195 - Currently set apparent power limit (VA)',40195,'U32','FIX0'],
#  ['40200 - Operating mode of stat.V stab., stat.V stab. config.',40200,'U32','ENUM'],
#  ['40204 - Reactive power set value as a % (%)',40204,'S32','FIX1'],
#  ['40206 - cosPhi setpoint, cosPhi config., direct specif.',40206,'S32','FIX2'],
#  ['40208 - cosPhi excit.type, cosPhi config., direct spec.',40208,'U32','ENUM'],
#  ['40210 - Operating mode of feed-in management',40210,'U32','ENUM'],
#  ['40212 - Active power limitation P, active power configuration (W)',40212,'U32','FIX0'],
#  ['40214 - Active power limitation P, active power configuration (%)',40214,'U32','FIX0'],
#  ['40216 - Operating mode of active power reduction in case of overfrequency P(f)',40216,'U32','ENUM'],
#  ['40218 - Difference between starting frequency and grid frequency, linear instantaneous power gradient configuration (Hz)',40218,'U32','FIX2'],
#  ['40220 - Difference between reset frequency and grid frequency, linear instantaneous power gradient configuration (Hz)',40220,'U32','FIX2'],
#  ['40222 - cosPhi at start point, cosPhi(P) char. config.',40222,'U32','FIX2'],
#  ['40224 - Excit. type at start point, cosPhi(P) char. conf.',40224,'U32','ENUM'],
#  ['40226 - cosPhi at end point, cosPhi(P) char. config.',40226,'U32','FIX2'],
#  ['40228 - Excit. type at end point, cosPhi(P) char. config.',40228,'U32','ENUM'],
#  ['40230 - Act. power at start point, cosPhi(P) char. config. (%)',40230,'U32','FIX0'],
#  ['40232 - Act. power at end point, cosPhi(P) char. config. (%)',40232,'U32','FIX0'],
#  ['40238 - Active power gradient, linear instantaneous power gradient configuration (%)',40238,'U32','FIX0'],
#  ['40240 - Activation of stay-set indicator function, linear instantaneous power gradient configuration',40240,'U32','ENUM'],
#  ['40242 - Active power gradient after reset frequency, linear instantaneous power gradient configuration (%)',40242,'U32','FIX0'],
#  ['40428 - Frequency monitoring median maximum threshold (Hz)',40428,'U32','FIX2'],
#  ['40430 - Frq. monitoring median max. threshold trip. time (ms)',40430,'U32','FIX0'],
#  ['40432 - Frequency monitoring lower maximum threshold (Hz)',40432,'U32','FIX2'],
#  ['40434 - Frq. monitoring lower max. threshold trip. time (ms)',40434,'U32','FIX0'],
#  ['40436 - Frequency monitoring upper minimum threshold (Hz)',40436,'U32','FIX2'],
#  ['40438 - Frq. monitoring upper min. threshold trip. time (ms)',40438,'U32','FIX0'],
#  ['40440 - Frequency monitoring median minimum threshold (Hz)',40440,'U32','FIX2'],
#  ['40442 - Frq. monitoring median min. threshold trip. time (ms)',40442,'U32','FIX0'],
#  ['40448 - Voltage monitoring median maximum threshold (V)',40448,'U32','FIX2'],
#  ['40450 - Voltage monitoring median max. threshold trip.time (ms)',40450,'U32','FIX0'],
#  ['40452 - Voltage monitoring lower maximum threshold (V)',40452,'U32','FIX2'],
#  ['40456 - Voltage monitoring lower max. threshold trip. time (ms)',40456,'U32','FIX0'],
#  ['40458 - Voltage monitoring lower minimum threshold (V)',40458,'U32','FIX2'],
#  ['40462 - Voltage monitoring lower min. threshold trip. time (ms)',40462,'U32','FIX0'],
#  ['40464 - Voltage monitoring of median minimum threshold (V)',40464,'U32','FIX2'],
#  ['40466 - Voltage monitoring median min. threshold trip.time (ms)',40466,'U32','FIX0'],
#  ['40470 - Island network detect. status',40470,'U32','ENUM'],
#  ['40484 - Activation of active power gradient',40484,'U32','ENUM'],
#  ['40497 - MAC address',40497,'STR32','UTF8'],
#  ['40513 - Speedwire DNS server address',40513,'STR16','IP4'],
#  ['40631 - Device name',40631,'STR32','UTF8'],
#  ['40789 - Communication version',40789,'U32','REV'],
#  ['40915 - Set active power limit (W)',40915,'U32','FIX0'],
#  ['40999 - Setpoint cos(phi) as per EEI convention',40999,'S32','FIX4'], # Write only
#  ['41017 - Adjustment time of characteristic operating point, conf. of grid integr. char. 1 (s)',41017,'U32','FIX1'],
#  ['41023 - Number of points to be used, conf. of grid integr. char. 1',41023,'U32','FIX0'],
#  ['41025 - X-axes reference, conf. of grid integration char. 1',41025,'U32','ENUM'],
#  ['41027 - Y-axes reference, conf. of grid integration char. 1',41027,'U32','ENUM'],
#  ['41029 - X value 1, conf. of grid integr. char. 1',41029,'S32','FIX3'],
#  ['41031 - Y value 1, conf. of grid integr. char. 1',41031,'S32','FIX3'],
#  ['41033 - X value 2, conf. of grid integr. char. 1',41033,'S32','FIX3'],
#  ['41035 - Y value 2, conf. of grid integr. char. 1',41035,'S32','FIX3'],
#  ['41037 - X value 3, conf. of grid integr. char. 1',41037,'S32','FIX3'],
#  ['41039 - Y value 3, conf. of grid integr. char. 1',41039,'S32','FIX3'],
#  ['41041 - X value 4, conf. of grid integr. char. 1',41041,'S32','FIX3'],
#  ['41043 - Y value 4, conf. of grid integr. char. 1',41043,'S32','FIX3'],
#  ['41061 - 2nd characteristic curve number, configuration of characteristic curve mode',41061,'U32','FIX0'],
#  ['41063 - 2nd activation of the characteristic curve, configuration of characteristic curve mode',41063,'U32','ENUM'],
#  ['41065 - Adjustment time of char. operating point, conf. of grid integration char. 2 (s)',41065,'U32','FIX1'],
#  ['41071 - Number of points to be used, conf. of grid integr. char. 2',41071,'U32','FIX0'],
#  ['41073 - Input unit, conf. of grid integration char. 2',41073,'U32','ENUM'],
#  ['41075 - Output frequency, conf. of grid integration char. 2',41075,'U32','ENUM'],
#  ['41077 - X value 1, conf. of grid integr. char. 2',41077,'S32','FIX3'],
#  ['41079 - Y value 1, conf. of grid integr. char. 2',41079,'S32','FIX3'],
#  ['41081 - X value 2, conf. of grid integr. char. 2',41081,'S32','FIX3'],
#  ['41083 - Y value 2, conf. of grid integr. char. 2',41083,'S32','FIX3'],
#  ['41085 - X value 3, conf. of grid integr. char. 2',41085,'S32','FIX3'],
#  ['41087 - Y value 3, conf. of grid integr. char. 2',41087,'S32','FIX3'],
#  ['41089 - X value 4, conf. of grid integr. char. 2',41089,'S32','FIX3'],
#  ['41091 - Y value 4, conf. of grid integr. char. 2',41091,'S32','FIX3'],
#  ['41111 - Voltage monitoring of lower minimum threshold as RMS value (V)',41111,'U32','FIX2'],
#  ['41113 - Voltage monitoring of lower min.threshold as RMS value for tripping time (ms)',41113,'U32','FIX0'],
#  ['41115 - Voltage monitoring of upper maximum threshold as RMS value (V)',41115,'U32','FIX2'],
#  ['41117 - Voltage monitoring of upper max. thresh. as RMS value for tripping time (ms)',41117,'U32','FIX0'],
#  ['41121 - Set country standard',41121,'U32','FUNKTION_SEC'],
#  ['41123 - Min. voltage for reconnection (V)',41123,'U32','FIX2'],
#  ['41125 - Max. voltage for reconnection (V)',41125,'U32','FIX2'],
#  ['41127 - Lower frequency for reconnection (Hz)',41127,'U32','FIX2'],
#  ['41129 - Upper frequency for reconnection (Hz)',41129,'U32','FIX2'],
#  ['41169 - Minimum insulation resistance (Ohms)',41169,'U32','FIX0'],
#  ['41171 - Set total yield (kWh)',41171,'U32','FIX0'],
#  ['41173 - Set total operating time at grid connection point (h)',41173,'U32','Duration'],
#  ['41193 - Operating mode for absent active power limitation',41193,'U32','ENUM'],
#  ['41195 - Timeout for absent active power limitation (s)',41195,'U32','Duration'],
#  ['41197 - Fallback act power lmt P in % of WMax for absent act power lmt (%)',41197,'U32','FIX2'],
#  ['41199 - Set active power limit at grid connection point (%)',41199,'U32','FIX0'],
#  ['41203 - Nominal PV system power (W)',41203,'U32','FIX0'],
#  ['41217 - Set active power limit at grid connection point (W)',41217,'U32','FIX0'],
#  ['41219 - Operating mode for absent reactive power control',41219,'U32','ENUM'],
#  ['41221 - Timeout for absent reactive power control (s)',41221,'U32','Duration'],
#  ['41223 - Fallback react power Q in % of WMax for absent react power ctr (%)',41223,'S32','FIX2'],
#  ['41225 - Operating mode for absent cos Phi spec',41225,'U32','ENUM'],
#  ['41227 - Timeout for absent cos Phi spec (s)',41227,'U32','Duration'],
#  ['41229 - Fallback cos Phi for absent cos Phi spec',41229,'S32','FIX4'],
#  ['41253 - Fast shut-down',41253,'U32','ENUM'],
#  ['41255 - Normalized active power limitation by PV system ctrl (%)',41255,'S16','FIX2'],
#  ['41256 - Normalized reactive power limitation by PV system ctrl (%)',41256,'S16','FIX2'],
#  ['41257 - Setpoint cos(phi) as per EEI convention',41257,'S32','FIX4'],
#  ['43090 - Login with Grid Guard-Code',43090,'U32','FIX0']
  ]

# scan is not used for SMA inverters but solariot.py expects it to exist
scan = "{}"