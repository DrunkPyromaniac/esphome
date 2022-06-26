#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/remote_base/remote_base.h"

namespace esphome {
namespace tx141th_bv2 {

struct TX141TH_BV2Data
	{
	uint32_t humidity:8, temp:12, flags: 4, id:8;
	};

class TX141TH_BV2 : public Component, public remote_base::RemoteReceiverListener
	{
	public:
		void set_temperature_sensor(sensor::Sensor *temperature_sensor) { temperature_sensor_ = temperature_sensor; }
		void set_humidity_sensor(sensor::Sensor *humidity_sensor) { humidity_sensor_ = humidity_sensor; }
		void set_address(uint8_t address) { address_ = address; }
	protected:
		bool on_receive(remote_base::RemoteReceiveData src) override;

		sensor::Sensor *temperature_sensor_;
		sensor::Sensor *humidity_sensor_;

		uint8_t address_{0x00};
	};

}  // namespace tx141th_bv2
}  // namespace esphome
