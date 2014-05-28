/*
 * Copyright (c) 2008, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 *
 */

/**
 * \file 
 * 
 * Exceptions thrown by the code in the graph slam package
 *
 * \author Bhaskara Marthi
 */

#ifndef GRAPH_SLAM_EXCEPTION_H
#define GRAPH_SLAM_EXCEPTION_H

#include <ros/ros.h>
#include <boost/format.hpp>
#include <stdexcept>

namespace graph_slam
{

using boost::format;

/// Base class for all graph_slam exceptions
struct GraphSlamException: public std::logic_error
{
  GraphSlamException (const format& error_string) : std::logic_error(error_string.str()) {};
  GraphSlamException (const char* str) : std::logic_error(str) {};
};


/// \brief Localization buffer doesn't contain localizations surrounding time t
struct LocalizationExtrapolationException: public GraphSlamException
{
  LocalizationExtrapolationException (const ros::Time& t) :
    GraphSlamException (format ("Couldn't extrapolate localization at time %1% as localization buffer was empty") % t) {}

  LocalizationExtrapolationException (const ros::Time& t, const ros::Time& nearest) :
    GraphSlamException (format ("Couldn't extrapolate localization at time %1%; nearest localization was at %2%")
                        % t % nearest) {}

  
};

/// \brief Exception for when we time out waiting for localization
struct LocalizationTimeoutException: public GraphSlamException
{
  LocalizationTimeoutException (const ros::Time& t, const ros::Duration& d) : 
    GraphSlamException (format ("Timed out after waiting %1% for localization at time %2%") % d % t) {}
};      


} // namespace

#endif // include guard
